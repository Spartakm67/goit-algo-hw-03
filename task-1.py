from datetime import datetime

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

def get_days_from_today(date):

    try:
        today = datetime.today().date()
        print(f"Today is: {today}")

        given_date = string_to_date(date)

        delta_days = (today - given_date).days
                
        return delta_days

    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD")


user_input = input("Enter date in (YYYY-MM-DD) format: ")
result = get_days_from_today(user_input)

if result is not None:
    print(f"Difference in days: {result}")



