from datetime import date

today_year = date.today().year
august_first_day = date(today_year, 8, 1)
first_saturday = date(today_year, 8, august_first_day.day + (5 - august_first_day.weekday()))

print(first_saturday)

