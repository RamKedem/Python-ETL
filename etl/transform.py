import logging


class Transformer:

    def __init__(self, data_type, data_name, df):
        self.data = df
        self.data_name = data_name
        self.logger = logging.getLogger(__name__)
        funcname = data_type + '_' + data_name
        getattr(self, funcname)()

    def csv_campaigns(self):
        try:
            self.logger.info(f'{self.data_name} - Initiating Transorm')
            self.modified_data = self.data
            self.logger.info(f'{self.data_name} transformed successfully')
        except:
            self.logger.error(f'Unable to transform {self.data_name}\n{e}')

    def csv_crypto(self):
        try:
            self.logger.info(f'{self.data_name} - Initiating Transorm')
            self.modified_data = self.data
            self.logger.info(f'{self.data_name} transformed successfully')
        except:
            self.logger.error(f'Unable to transform {self.data_name}\n{e}')

    def csv_sf_crimes(self):
        try:
            self.logger.info(f'{self.data_name} - Initiating Transorm')
            self.modified_data = self.data
            self.logger.info(f'{self.data_name} transformed successfully')
        except:
            self.logger.error(f'Unable to transform {self.data_name}\n{e}')

    def excel_webpharm(self):
        try:
            self.logger.info(f'{self.data_name} - Initiating Transorm')
            self.modified_data = self.data
            self.logger.info(f'{self.data_name} transformed successfully')
        except:
            self.logger.error(f'Unable to transform {self.data_name}\n{e}')