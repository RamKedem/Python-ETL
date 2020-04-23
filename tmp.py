from datetime import date, timedelta

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


print(generate_range_dates('22_04_2020', '25_04_2020'))