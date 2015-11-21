import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('Dashboard-c5a20a37defa.json'))  # File with credentials
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)


def sendToSheet(cell, number):
    """Send data to sheet"""
    sheet = "DashBoard Data"  # Name of Google Sheet
    wks = gc.open(sheet).sheet1
    wks.update_acell(cell, number)
    cell_list = wks.range('A1:B7')
