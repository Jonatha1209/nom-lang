from parse_nom import parse_nom

class NomFileManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.context = {}
        self._load()

    def _load(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                text = f.read()
                self.context = parse_nom(text)
        except FileNotFoundError:
            self.context = {}

    def read(self):
        return self.context

    def write(self, key, value, type_):
        self.context[key] = {
            "value": value,
            "type": type_
        }

    def update(self, key, value, type_=None):
        if key in self.context:
            self.context[key]["value"] = value
            if type_:
                self.context[key]["type"] = type_
        else:
            raise KeyError(f"{key} not found in .nom file")

    def delete(self, key):
        if key in self.context:
            del self.context[key]
        else:
            raise KeyError(f"{key} not found in .nom file")

    def save(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write("{\n")
            for key, data in self.context.items():
                val = data["value"]
                typ = data["type"]
                formatted_val = self._format_value(val)
                f.write(f"  {key} : {formatted_val} -> {typ},\n")
            f.write("}\n")

    def _format_value(self, val):
        if isinstance(val, str):
            return f'"{val}"'
        elif isinstance(val, bool):
            return "true" if val else "false"
        elif isinstance(val, list):
            inner = ", ".join([self._format_value(v) for v in val])
            return f"[{inner}]"
        else:
            return str(val)
