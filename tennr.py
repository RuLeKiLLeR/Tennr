
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import gspread
import pandas as pd

# Authenticate with Google Sheets
client = gspread.oauth()  # Use your authentication method here

# Specify the details
spreadsheet_id = "###"  # Please put your Spreadsheet ID.
sheet_name = "Sheet3"  # Please put the name of the sheet you want to use.
csv_file = "###"  # Please put the file path of the CSV file you want to use.


def Export_Data_To_Sheets(dataframe):
    spreadsheet = client.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.worksheet(sheet_name)
    values = dataframe.values.tolist()
    worksheet.update(values)

def table_fetcher(url,index):
    tables = pd.read_html(url)
    Export_Data_To_Sheets(tables[index])



