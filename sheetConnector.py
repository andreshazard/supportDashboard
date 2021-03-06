import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials
import sys
import os

try:
    json_key = json.load(open(os.path.join(os.path.dirname(__file__), 'Dashboard-c5a20a37defa.json')))  # File with credentials located on same path as main.py
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
    gc = gspread.authorize(credentials)
except:
    sys.exit('Error connecting to Google Sheet, check if json file is present and active on Google')


def send_to_sheet(cell, number):
    """Send data to sheet"""
    try:
        sheet = "DashBoard Data"  # Name of Google Sheet
        wks = gc.open(sheet).sheet1
        wks.update_acell(cell, number)
        cell_list = wks.range('A1:B7')
    except:
        sys.exit('Error sending  data to sheet, check cell location')
