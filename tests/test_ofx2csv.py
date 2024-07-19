import os

import pytest
import yaml

from ofx2csv.ofx2csv import reorder_fields


def test_reorder_fields():
    # Input dictionary with fields not in order
    input_line = {
        "payee": "John Doe",
        "amount": 100,
        "date": "2023-04-01",
        "checknum": "123",
        "type": "DEBIT",
        "id": "abc123",
        "account_id": "xyz789",
        "account_type": "CHECKING",
    }

    # Expected dictionary with fields in order
    expected_line = {
        "date": "2023-04-01",
        "checknum": "123",
        "payee": "John Doe",
        "amount": 100,
        "type": "DEBIT",
        "id": "abc123",
        "account_id": "xyz789",
        "account_type": "CHECKING",
    }

    # Call the function with the input dictionary
    result_line = reorder_fields(input_line)

    # Assert that the result matches the expected output
    assert result_line == expected_line, "The fields were not reordered correctly."
