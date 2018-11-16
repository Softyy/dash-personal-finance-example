from datetime import datetime as dt

DATA_COLUMNS = ['Date','Vendor','Charge','Credit','Total Balance']
DATA_DATE = DATA_COLUMNS[0]
DATA_CHARGE = DATA_COLUMNS[2]
DATA_VENDOR = DATA_COLUMNS[1]

WEBAPP_TITLE = 'My Personal Finances'
WEBAPP_SUBTITLE = "This is a place where I see my money leaving me..."
WEBAPP_GRAPH_TITLE = "My Daily Visa Spending"

DATA_MANAGER_NO_DATA = 'Data must be loaded into DataManager'
DATA_MANAGER_KEY_ERROR = 'Column names of your data do not match your keys'

VENDOR_TEST_OPTIONS = [
    {'label': 'All', 'value': 0},
    {'label': 'Vendor 1', 'value': 1},
    {'label': 'Vendor 2', 'value': 2},
    {'label': 'Vendor 3', 'value': 3}
]

VENDOR_SELECTOR_ID = 'vendor-selection'

OUTPUT_GRAPH_ID = 'output-graph'

MIN_DATE_SELECTOR = dt(2017,10,10)
