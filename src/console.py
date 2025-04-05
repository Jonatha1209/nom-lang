from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
import json
from main import NomFileManager
from nom_config import load_nomrc

base_commands = [
    "read", "write", "update", "delete",
    "eval", "to-json", "to-sql", "validate", "help", "end", "exit"
]

def main():
    user_config = load_nomrc()
    filepath = user_config.get("default_file") or input("Enter path to .nom file: ").strip()
    prompt_color = user_config.get("prompt_color", "green")
    auto_save = user_config.get("auto_save", True)
    default_table = user_config.get("default_table", "my_table")

    style = Style.from_dict({
        "prompt": f"{prompt_color} bold",
    })


    manager = NomFileManager(filepath)
    session = PromptSession()
    command_completer = WordCompleter(base_commands, ignore_case=True)

    print(f"\n.nom CLI for {filepath}")
    print("Type 'help' for commands. Type 'end' to exit.\n")

    while True:
        try:
            user_input = session.prompt("[.nom] >>> ", completer=command_completer, style=style).strip()
            if not user_input:
                continue

            if user_input.lower() in {"end", "exit", "quit"}:
                print("👋 Bye!")
                break

            args = user_input.split()
            cmd = args[0]
            context = manager.read()

            if cmd == "help":
                _show_help()

            elif cmd == "read":
                for k, v in context.items():
                    print(f"{k}: {v['value']} ({v['type']})")

            elif cmd == "write" and len(args) >= 4:
                key, value, type_ = args[1], args[2], args[3]
                manager.write(key, _auto_cast(value, type_), type_)
                if auto_save:
                    manager.save()
                print(f"[+] {key} added.")

            elif cmd == "update" and len(args) >= 3:
                key, value = args[1], args[2]
                type_ = args[3] if len(args) > 3 else context[key]["type"]
                manager.update(key, _auto_cast(value, type_), type_)
                if auto_save:
                    manager.save()
                print(f"[~] {key} updated.")

            elif cmd == "delete" and len(args) >= 2:
                key = args[1]
                manager.delete(key)
                if auto_save:
                    manager.save()
                print(f"[-] {key} deleted.")

            elif cmd == "to-json":
                print(json.dumps({k: v["value"] for k, v in context.items()}, indent=2))

            elif cmd == "to-sql":
                table = args[1] if len(args) > 1 else default_table
                keys = ", ".join(context.keys())
                values = ", ".join(_sql_format(v["value"], v["type"]) for v in context.values())
                print(f"INSERT INTO {table} ({keys}) VALUES ({values});")

            elif cmd == "eval":
                for k, v in context.items():
                    print(f"{k} = {v['value']} ({v['type']})")

            elif cmd == "validate":
                valid = True
                for k, v in context.items():
                    if not _validate_type(v["value"], v["type"]):
                        print(f"[!] Invalid type for key '{k}': expected {v['type']}, got {type(v['value']).__name__}")
                        valid = False
                if valid:
                    print("✅ .nom file is valid!")

            else:
                print(f"[!] Unknown or malformed command: {cmd}")

        except Exception as e:
            print(f"[!] Error: {e}")


def _show_help():
    print("""
🛠 Available Commands:
  write <key> <value> <type>     Add new value
  update <key> <value> [type]    Update existing value
  delete <key>                   Delete a key
  read                           Print .nom values
  to-json                        Convert to JSON
  to-sql [table]                 Convert to SQL INSERT
  eval                           Evaluate values/functions
  validate                       Validate types
  end / exit                     Exit the CLI
""")


def _auto_cast(value, type_):
    if type_ == "integer":
        return int(value)
    elif type_ == "float":
        return float(value)
    elif type_ == "boolean":
        return value.lower() == "true"
    elif type_ == "list":
        return [v.strip() for v in value.strip('[]').split(',')]
    return value


def _sql_format(val, type_):
    if type_ == "string":
        return f"'{val}'"
    if type_ == "boolean":
        return "TRUE" if val else "FALSE"
    if type_ == "list":
        return f"'{json.dumps(val)}'"
    return str(val)


def _validate_type(value, type_):
    return {
        "string": lambda x: isinstance(x, str),
        "integer": lambda x: isinstance(x, int),
        "float": lambda x: isinstance(x, float),
        "boolean": lambda x: isinstance(x, bool),
        "list": lambda x: isinstance(x, list),
    }.get(type_, lambda x: True)(value)


if __name__ == "__main__":
    main()
