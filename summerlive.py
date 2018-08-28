from datetime import date

def first_saturday(weekday):
    if weekday == 6:
        saturday = 8 + (5 - weekday)
    else:
        saturday = 1 + (5 - weekday)
    return saturday

if __name__ == '__name__':
    today_year = date.today().year

    for next_year in range(10):
        august_firstday = date(today_year + next_year, 8, 1)
        print('{0.year}/{0.month}/{1}'.format(august_firstday, first_saturday(august_firstday.weekday())))
