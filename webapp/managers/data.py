import os
import pandas as pd

from ..consts import DATA_COLUMNS,DATA_DATE,DATA_CHARGE,DATA_MANAGER_KEY_ERROR,DATA_MANAGER_NO_DATA

class DataManager():

    def load_csv_data(self,filepath):
        self.data = pd.read_csv(filepath,names=DATA_COLUMNS)

    def load_test_data(self):
        self.load_csv_data(os.path.join(os.getcwd(),"webapp","test_data","Jan-2018.csv"))
    
    def get_charge_series_tuple(self):
        """ 
        Separates the date and charge values for easy plotting from the loaded data.

        returns (date_array,charge_array)
        """
        try:
            series = self.data.groupby([DATA_DATE]).sum()[DATA_CHARGE]
            return (series.index.values,series.values)
        except AttributeError:
            raise Exception(DATA_MANAGER_NO_DATA)
        except KeyError:
            raise Exception(DATA_MANAGER_KEY_ERROR)
