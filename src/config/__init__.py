from yaml import safe_load
with open("src/config/Config.yml", "r") as config_file:
    CONFIG = safe_load(config_file)
