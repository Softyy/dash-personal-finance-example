import os, glob
import pandas as pd
from datetime import datetime as dt

from webapp import cache,db
from ..consts import DATA_COLUMNS,DATA_DATE,DATA_CHARGE,DATA_MANAGER_KEY_ERROR,DATA_MANAGER_NO_DATA,DATA_VENDOR,MIN_DATE_SELECTOR,MAX_DATE_SELECTOR,TRANSACTION_TABLE_NAME

class DataManager():

    def load_data(self):
        files_path = os.path.join(os.getcwd(),"webapp","test_data")
        all_files = glob.glob(os.path.join(files_path, "*.csv"))
        self.data = pd.concat((pd.read_csv(f,names=DATA_COLUMNS) for f in all_files))
        self.data[DATA_DATE] = pd.to_datetime(self.data[DATA_DATE]).dt.date

    @cache.memoize()
    def load_from_db(self):
        with db.engine.connect() as conn, conn.begin():
            return pd.read_sql(TRANSACTION_TABLE_NAME,conn)
    
    def get_charge_series_tuple(self,data=pd.DataFrame(),min_date=None,max_date=None):
        """ 
        Input: pd.DataFrame, if none is provided it defaults to self.data
        
        Separates the date and charge values for easy plotting from the loaded data.

        returns (date_array,charge_array)
        """
        # take the default argument to be the data frame within the manager.
        if data.empty:
            data = self.load_from_db()
        
        if min_date == None:
            min_date = min(self.load_from_db()[DATA_DATE])

        if max_date == None:
            max_date = max(self.load_from_db()[DATA_DATE])

        try:
            series = data.groupby([DATA_DATE]).sum()[DATA_CHARGE]
            index_range = pd.date_range(min_date,max_date)
            series = series.reindex(index_range,fill_value=0)
            return (series.index,series.values)
        except AttributeError:
            raise Exception(DATA_MANAGER_NO_DATA)
        except KeyError:
            raise Exception(DATA_MANAGER_KEY_ERROR)

    def get_vendor_options(self):
        vendors = self.load_from_db()[DATA_VENDOR].unique()
        options = [{'label':'All','value':0}]
        options.extend([{'label':vendors[n],'value':n+1} for n in range(0,len(vendors))])
        return options

    def get_selected_charge_series_tuple(self,selection = [0],min_date=MIN_DATE_SELECTOR,max_date=MAX_DATE_SELECTOR):
        vendors = self.load_from_db()[DATA_VENDOR].unique()
        selected_vendors = [element for index, element in enumerate(vendors) if index+1 in selection]
        filtered_data = self.load_from_db()[self.load_from_db()[DATA_VENDOR].isin(selected_vendors)] if not 0 in selection else self.load_from_db()
        return self.get_charge_series_tuple(filtered_data,min_date,max_date)