from gshclass import *
import pytest
import os

# testing constructor of GoogleSheetHelper class
cred_path = "/home/batman/Desktop/learning_to_test_code/unit_test_boiler_builtin/master_key.json"
#cred_path = os.environ.get("CRED_JSON")

# test constructor
def test_make_gsh_helper():
    gsh1 = GoogleSheetHelper(cred_path, "google_postgres", "existing")
    assert gsh1.cred_json == cred_path
    assert gsh1.spreadsheetName == "google_postgres"
    assert gsh1.sheetName == "existing"
