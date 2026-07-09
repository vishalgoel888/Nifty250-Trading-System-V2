import os

# ==========================
# Google Sheet Configuration
# ==========================

SPREADSHEET_ID = "179wbmjWyaiSFdMe6oaZ3ERV59u7PA20adTualvjfvGI"

DASHBOARD_SHEET = "Dashboard"
MASTER_SHEET = "Nifty250 Master"
DATA_SHEET = "Nifty250 Data"
INDICATOR_SHEET = "Indicators"
PORTFOLIO_SHEET = "Portfolio"
SETTINGS_SHEET = "Settings"
LOG_SHEET = "Logs"

# ==========================
# GitHub Secret
# ==========================

GCP_CREDENTIALS = os.environ.get("GCP_CREDENTIALS")