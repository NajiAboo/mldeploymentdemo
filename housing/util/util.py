import yaml
import os, sys
from housing.exception import HousingException

def read_yaml_file(file_path:str) -> dict:
    try:

        with open(file_path, "rb") as yaml_file:
            config_info = yaml.safe_load(yaml_file)
        return config_info
    except Exception as e:
        raise HousingException(e,sys) from e