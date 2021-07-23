from gshclass import *
import pytest
import os
from dotenv import load_dotenv

# creds
load_dotenv()
cred_path = os.environ.get("CRED_PATH")

# testing constructor of GoogleSheetHelper class
def test_make_gsh_helper():
    gsh1 = GoogleSheetHelper(cred_path, "google_postgres", "existing")
    assert gsh1.cred_json == cred_path
    assert gsh1.spreadsheetName == "google_postgres"
    assert gsh1.sheetName == "existing"
