import os
import configparser

def load_nomrc():
    config = configparser.ConfigParser()
    rc_path = os.path.expanduser("~/.nomrc")

    if os.path.exists(rc_path):
        config.read(rc_path)
    else:
        return {}

    result = {}
    if "DEFAULT" in config:
        for key in config["DEFAULT"]:
            val = config["DEFAULT"][key]
            if val.lower() in ("true", "false"):
                val = val.lower() == "true"
            result[key] = val
    return result
