import engine
import logging.config
import sys
import datetime
from datetime import date, timedelta


def validate_date_text(date_text):
    try:
        valid_date = datetime.datetime.strptime(date_text, '%d_%m_%Y')
        return valid_date.strftime("%d_%m_%Y")
    except ValueError:
        print("Incorrect data format, should be DD_MM_YYYY")
        sys.exit(1)


def generate_range_dates(begin_date, e_date):
    s_day,s_month,s_year = [int(date_part) for date_part in begin_date.split('_')]
    e_day,e_month,e_year = [int(date_part) for date_part in e_date.split('_')]
    s_date = date(s_year,s_month,s_day)
    e_date = date(e_year,e_month,e_day)

    dates = []
    delta = e_date - s_date

    for i in range(delta.days + 1):
        day = s_date + timedelta(days=i)
        dates.append(day.strftime("%d_%m_%Y"))

    return dates


def args_check():
    if len(sys.argv) != 3:
        print("Usage : range_load.py START_DATE END_DATE")
        sys.exit(1)
    else:
        s_date = validate_date_text(sys.argv[1])
        e_date = validate_date_text(sys.argv[2])
        return generate_range_dates(s_date, e_date)


def main(process_date):
    engine.engine(process_date)


if __name__ == '__main__':
    range_of_dates = args_check()
    logging.config.fileConfig('conf/logging_config.conf')
    logger = logging.getLogger(__name__)
    logger.info(f'======== Executing Range Process ========')
    logger.info(f'{range_of_dates[0]} - {range_of_dates[-1]}')

    for date in range_of_dates:
        main(process_date=date)