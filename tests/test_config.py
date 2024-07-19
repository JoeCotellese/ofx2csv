import os

import pytest
import yaml

from ofx2csv.config import Config


# Fixture to create a temporary config file and Config instance
@pytest.fixture
def temp_config(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "config.yml"
    config_data = {
        "config": {
            "ignored_fields": ["password", "secret"],
            "payees": [
                {"name": "Payee1", "patterns": ["^P1.*"]},
                {"name": "Payee2", "patterns": ["^P2.*"]},
            ],
        }
    }
    with open(p, "w") as config_file:
        yaml.dump(config_data, config_file)
    return Config(str(p))


# Test initialization and loading of the config file
def test_config_initialization(temp_config):
    assert temp_config.config_file is not None
    assert "config" in temp_config.config
    assert "ignored_fields" in temp_config.config["config"]
    assert "payees" in temp_config.config["config"]


# Test get_ignored_fields method
def test_get_ignored_fields(temp_config):
    ignored_fields = temp_config.get_ignored_fields()
    assert isinstance(ignored_fields, list)
    assert "password" in ignored_fields
    assert "secret" in ignored_fields


# Test allowed_field method
def test_allowed_field(temp_config):
    assert temp_config.allowed_field("username") is True
    assert temp_config.allowed_field("password") is False


# Test get_payees method
def test_get_payees(temp_config):
    payees = temp_config.get_payees()
    assert isinstance(payees, list)
    assert len(payees) == 2
    assert payees[0]["name"] == "Payee1"
    assert payees[1]["name"] == "Payee2"


# Test match_payee method
def test_match_payee(temp_config):
    assert temp_config.match_payee("P1-123") == "Payee1"
    assert temp_config.match_payee("P2-456") == "Payee2"
    assert temp_config.match_payee("Unknown") == "Unknown"
