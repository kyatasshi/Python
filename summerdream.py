from datetime import date

today_year = date.today().year
today_sat = date(today_year, 8, 1)
day = date(today_year, 8, today_sat.day + (5 - today_sat.weekday()))

print(day)

