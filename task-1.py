from datetime import datetime

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

def get_days_from_today(date):

    today =  datetime.today().date()
    print(today)

    given_data = string_to_date(date)

    delta_days = (today - given_data).days
    print(delta_days)
    
    return delta_days



get_days_from_today("2021-10-09")



