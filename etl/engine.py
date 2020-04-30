from etl.extract import *
from etl.transform import *
from etl.load import *
from conf.credentials import *
import logging.config
import logging


def engine(date):
    logger = logging.getLogger(__name__)

    etl_data = json.load(open('conf/sources_config.json'))

    logger.info(f"======== Initiating ETL Process for {date} ========")

    destination = SQLServer(sql_server_target['server'],
                            sql_server_target['instance'],
                            sql_server_target['database'],
                            sql_server_target['driver'])

    extractor = Extractor()
    for source_type, source_names in etl_data['data_sources'].items():
        for source_name in source_names:
            if source_type == 'csv':
                df = extractor.get_csv_data(date,source_name)
            elif source_type == 'excel':
                df = extractor.get_excel_data(date,source_name)

            if df is not None:
                t = Transformer(source_type,source_name,df)
                destination.insert_with_progress(t.modified_data,source_name)


if __name__ == '__main__':
    engine()