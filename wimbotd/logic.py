import datetime

forbidden_months = [4,6,9,11]
forbidden_day = 31

forbidden_days_feb = [30, 31]

def process(date, month, weekday):

    fail = "Please go back and enter a valid date."

    if date in forbidden_days_feb and month == 2:
        return fail
    elif date == forbidden_day and month in forbidden_months:
        return fail

    weekday = weekday.capitalize()

    today = datetime.datetime.now()

    if date == 29 and month == 2:
        diff = 2024 - today.year
        year = 2024
        years = diff

    else:
        year = int(today.year)
        years = 0

    while datetime.datetime(year, month, date).strftime("%A") != weekday:

        if date == 29 and month == 2:
            year += 4
            years += 4

        else:
            year += 1
            years += 1

    if date == 29 and month == 2:
        egg = ", you leapling."
        
    else:
        egg = "."

    if (years == 0):
        return f"You will have your birthday on {weekday} this year" + egg

    elif (years == 1):
        return f"You will have your birthday on {weekday} next year" + egg
    
    else:
        return f"You will have your birthday on {weekday} in {years} years time, in the year {year}" + egg
