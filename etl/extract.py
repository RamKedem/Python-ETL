import pandas as pd
import json
import logging
import glob

class Extractor:

    def __init__(self):
        self.data_sources = json.load(open('conf/sources_config.json'))
        self.csv_path = self.data_sources['data_sources']['csv']
        self.excel_path = self.data_sources['data_sources']['excel']
        self.logger = logging.getLogger(__name__)

    def get_csv_data(self, date, csv_name):
        return self._get_core(date, csv_name, "csv")

    def get_excel_data(self, date, excel_name):
        return self._get_core(date, excel_name, "excel")

    def _get_core(self, date, filename, mode="csv"):
        try:
            self.logger.info(f'{filename} - Initiating extraction')
            if mode == "excel":
                full_path = f'data/{date}/{self.excel_path[filename]}/*.xlsx'
            elif mode == "csv":
                full_path = f'data/{date}/{self.csv_path[filename]}/*.csv'
            else:
                full_path = f'data/{date}/{self.csv_path[filename]}/*.csv'

            filenames = glob.glob(full_path)

            if len(filenames) == 0:
                self.logger.info(f'No valid files found on {full_path}')
                return

            if mode == "excel":
                list_of_dfs = [pd.read_excel(filename) for filename in filenames]
            elif mode == "csv":
                list_of_dfs = [pd.read_csv(filename) for filename in filenames]
            else:
                list_of_dfs = [pd.read_csv(filename) for filename in
                               filenames]

            self.logger.info(f'{filename} extracted successfully')
            return pd.concat(list_of_dfs)

        except Exception as e:
            self.logger.error(f'Unable to load {filename}\n{e}')
            return

