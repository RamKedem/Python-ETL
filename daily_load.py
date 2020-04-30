import sys

from etl import engine
import logging.config
import logging

import datetime


def validate_date_text(date_text):
    try:
        valid_date = datetime.datetime.strptime(date_text, '%d_%m_%Y')
        return valid_date.strftime("%d_%m_%Y")
    except ValueError:
        print("Incorrect data format, should be DD_MM_YYYY")
        sys.exit(1)


def args_check():
    if len(sys.argv) > 2:
        print("Usage options :")
        print("1. daily_load.py")
        print("2. daily_load.py DD_MM_YYYY")
        sys.exit(1)
    elif len(sys.argv) == 2:
        current_date = validate_date_text(sys.argv[1])
    elif len(sys.argv) == 1:
        current_date = datetime.datetime.now().strftime("%d_%m_%Y")
    return current_date


def main(process_date):
    logging.config.fileConfig('conf/logging_config.conf')
    logger = logging.getLogger(__name__)
    logger.info(f'{"="*8} Executing Daily Process {"="*8}')
    engine.engine(process_date)

if __name__ == '__main__':
    date = args_check()
    main(process_date=date)