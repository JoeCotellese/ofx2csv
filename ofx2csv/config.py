"""
File: config.py
Author: Joe Cotellese
Description: This module is responsible for providing application configuration
to the rest of the app.

The config file is in yaml format.

Example config file:
config:
    ignored_fields:
        - branch_id
        - mcc
        - memo
        - curdef
"""

import logging

import yaml

logger = logging.getLogger(__name__)


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=SingletonMeta):
    def __init__(self, config_file: str = "config.yml"):
        self.config_file = config_file
        logger.info("Loading config file: {}".format(self.config_file))
        self.config = self.load_config()

    def load_config(self) -> dict:
        with open(self.config_file, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logger.error(exc)
                print(exc)

    def get_ignored_fields(self) -> list:
        if "ignored_fields" not in self.config["config"]:
            return []
        return self.config["config"]["ignored_fields"]

    def allowed_field(self, field: str) -> bool:
        return field not in self.get_ignored_fields()
