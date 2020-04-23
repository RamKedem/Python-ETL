import pandas as pd
import json
import logging
import glob


class Extract:

    def __init__(self):
        self.data_sources = json.load(open('conf/sources_config.json'))
        self.csv_path = self.data_sources['data_sources']['csv']
        self.excel_path = self.data_sources['data_sources']['excel']
        self.logger = logging.getLogger(__name__)

    def get_csv_data(self, date, csv_name):
        try:

            self.logger.info(f'{csv_name} - Initiating Extract')
            full_path = f'data/{date}/{self.csv_path[csv_name]}/*.csv'
            filenames = glob.glob(full_path)

            if len(filenames)!=0:
                list_of_dfs = [pd.read_csv(filename) for filename in filenames]
                self.logger.info(f'{csv_name} extracted successfully')
                return pd.concat(list_of_dfs)
            else:
                self.logger.info(f'No csv files found on {full_path}')
                return None

        except Exception as e:
            self.logger.error(f'Unable to load {csv_name}\n{e}')
            return None

    def get_excel_data(self, date, excel_name):
        try:

            self.logger.info(f'{excel_name} - Initiating Extract')
            full_path = f'data/{date}/{self.excel_path[excel_name]}/*.xlsx'
            filenames = glob.glob(full_path)

            if len(filenames) != 0:
                list_of_dfs = [pd.read_excel(filename) for filename in filenames]
                self.logger.info(f'{excel_name} extracted successfully')
                return pd.concat(list_of_dfs)
            else:
                self.logger.info(f'No excel files found on {full_path}')
                return None

        except Exception as e:
            self.logger.error(f'Unable to load {excel_name}\n{e}')
            return None
