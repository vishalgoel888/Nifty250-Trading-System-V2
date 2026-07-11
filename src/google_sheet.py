import json
import os
from pathlib import Path

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from src.config import SPREADSHEET_ID


def connect_sheet():

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds_json = os.environ.get("GCP_CREDENTIALS")

    if creds_json:

        creds_dict = json.loads(creds_json)

        creds = ServiceAccountCredentials.from_json_keyfile_dict(
            creds_dict,
            scope
        )

    else:

        json_path = Path("credentials/service_account.json")

        if not json_path.exists():
            raise Exception("service_account.json not found")

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            str(json_path),
            scope
        )

    client = gspread.authorize(creds)

    return client.open_by_key(SPREADSHEET_ID)


def write_dataframe(sheet, worksheet_name, df):

    worksheet = sheet.worksheet(worksheet_name)

    worksheet.clear()

    # Copy dataframe
    df = df.copy()

    # Convert Date column to string
    if "Date" in df.columns:
        df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

    # Convert NaN values to blank
    df = df.fillna("")

    # Prepare data for Google Sheets
    data = [df.columns.tolist()] + df.values.tolist()

    worksheet.update(
        values=data,
        range_name="A1"
    )

    print(f"{worksheet_name} updated successfully.")


def read_symbols(sheet):

    worksheet = sheet.worksheet("Nifty250 Master")

    records = worksheet.get_all_records()

    symbols = []

    for row in records:

        symbol = row.get("Symbol")

        if symbol:
            symbols.append(f"{symbol}.NS")

    return symbols