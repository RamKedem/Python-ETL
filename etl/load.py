import pandas as pd
from sqlalchemy import create_engine
import time
from tqdm import tqdm
from etl.helpers import *

class SQLServer():

    def __init__(self, server, instance, database, driver, user=None, password=None):
        self.user = user
        self.password = password
        self.server = server
        self.instance = instance
        self.database = database
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.connect()

    @property
    def connection_string(self):
        if self.user and self.password:
            return f'mssql+pyodbc://{self.user}:{self.password}@{self.server}\{self.instance}/{self.database}?driver={self.driver}?Trusted_Connection=yes'
        else:
            return f'mssql+pyodbc://{self.server}\{self.instance}/{self.database}?driver={self.driver}?Trusted_Connection=yes'
        return url

    def connect(self):
        try:
            self.logger.info('Attempting to connect')
            self.engine = create_engine(self.connection_string, fast_executemany=True)
            self.logger.info('Connection successfull')
        except Exception as e:
            self.logger.error(f'Unable to connect\n{e}')
            print(self.connection_string)

    # deprecated in favor of insert_with_progress
    def insert(self, source_data, destination_table, schema='dbo'):
        if not isinstance(source_data, pd.DataFrame):
            self.logger.error('Unable to process datafile - not a DataFrame')
            return
        try:
            self.logger.info(f'Preparing to load into {destination_table}')
            start_time = time.time()
            source_data.to_sql(destination_table,
                               schema=schema,
                               con=self.engine,
                               if_exists='append',
                               index=False)
            self.logger.info(f"Insert completed successfully in {(time.time() - start_time)} seconds")
        except Exception as e:
            self.logger.error(f'Insert failed\n{e}')

    @staticmethod
    def chunker(seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    def insert_with_progress(self, source_data, destination_table, schema='dbo'):
        if not isinstance(source_data, pd.DataFrame):  # Invert logic to avoid nesting.
            self.logger.error('Unable to process datafile - not a DataFrame')
            return

        try:
            chunksize = int(len(source_data) / 10)
            tqdm_out = TqdmToLogger(self.logger, level=logging.INFO)
            with tqdm(total=len(source_data), file=tqdm_out) as pbar:
                start_time = time.time()
                self.logger.info(f'Inserting {len(source_data)} rows into {destination_table}')
                for cdf in self.chunker(source_data, chunksize):
                    cdf.to_sql(destination_table,
                               schema=schema,
                               con=self.engine,
                               if_exists='append',
                               index=False)
                    pbar.update(chunksize)
                self.logger.info(
                    f"{destination_table} - Insert completed successfully in {(time.time() - start_time)} seconds")
        except Exception as e:
            print(f'Insert into {destination_table} failed\n{e}')
