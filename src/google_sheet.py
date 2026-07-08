import json
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from src.config import SPREADSHEET_ID


def connect_sheet():
    creds_json = os.environ.get("GCP_CREDENTIALS")

    if not creds_json:
        raise Exception("GCP_CREDENTIALS not found")

    creds_dict = json.loads(creds_json)

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        creds_dict,
        scope
    )

    client = gspread.authorize(creds)

    return client.open_by_key(SPREADSHEET_ID)