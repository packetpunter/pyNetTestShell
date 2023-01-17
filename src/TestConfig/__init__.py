from yaml import safe_load
import os 

from yaml import safe_load

data_path = os.path.join(os.path.dirname(__file__), 'Config.yml')

with open(data_path) as config_file:
    CONFIG = safe_load(config_file)

