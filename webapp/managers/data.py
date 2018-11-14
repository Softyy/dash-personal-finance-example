import os, glob
import pandas as pd

from ..consts import DATA_COLUMNS,DATA_DATE,DATA_CHARGE,DATA_MANAGER_KEY_ERROR,DATA_MANAGER_NO_DATA,DATA_VENDOR

class DataManager():

    def load_data(self):
        path = os.path.join(os.getcwd(),"webapp","test_data")
        all_files = glob.glob(os.path.join(path, "*.csv"))
        self.data = pd.concat((pd.read_csv(f,names=DATA_COLUMNS) for f in all_files))
        self.data[DATA_DATE] = pd.to_datetime(self.data[DATA_DATE]).dt.date
    
    def get_charge_series_tuple(self):
        """ 
        Separates the date and charge values for easy plotting from the loaded data.

        returns (date_array,charge_array)
        """
        try:
            series = self.data.groupby([DATA_DATE]).sum()[DATA_CHARGE]
            return (series.index,series.values)
        except AttributeError:
            raise Exception(DATA_MANAGER_NO_DATA)
        except KeyError:
            raise Exception(DATA_MANAGER_KEY_ERROR)

    def get_vendor_options(self):
        vendors = self.data[DATA_VENDOR].unique()
        options = [{'label':'All','value':0}]
        options.extend([{'label':vendors[n],'value':n+1} for n in range(0,len(vendors))])
        return options