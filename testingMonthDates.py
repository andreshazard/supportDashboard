from datetime import date, timedelta, datetime
import calendar
import time
import datetime


def get_month_range(start_date=None):
# Return list of date from the begining of the month until today, in timestamp
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = date.today()
    a_day = timedelta(days=1)
    listOfDays = []
    while start_date < end_date:
        listOfDays.append(str(start_date))
        start_date += a_day
    newListOfDays = []
    for x in listOfDays:
        newListOfDays.append(time.mktime(time.strptime(x, "%Y-%m-%d")))
    return newListOfDays


def add_months(sourcedate,months):
    month = sourcedate.month - 1 + months
    year = int(sourcedate.year + month / 12 )
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    return datetime.date(year,month,day)


def getRangeOfLastThreeMonth():
    #Return a list with a date range of the last 3 month
    now = datetime.date.today()
    year = now.year
    month = now.month
    day = now.day
    date1 = add_months(now, -1)
    date2 = add_months(now, -2)
    date3 = add_months(now, -3)
    listOfDates = []
    listOfDates.append([str(date1.replace(day=01)), str(date1.replace(day=(calendar.monthrange(date1.year, date1.month)[1])))])
    listOfDates.append([str(date2.replace(day=01)), str(date2.replace(day=(calendar.monthrange(date2.year, date2.month)[1])))])
    listOfDates.append([str(date3.replace(day=01)), str(date3.replace(day=(calendar.monthrange(date3.year, date3.month)[1])))])
    newListOfDays = []
    for x in listOfDates:
        newListOfDays.append([time.mktime(time.strptime(x[0], "%Y-%m-%d")), time.mktime(time.strptime(x[1], "%Y-%m-%d"))])
    return newListOfDays


