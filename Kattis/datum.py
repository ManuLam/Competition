import datetime, calendar
d,m = map(int, input().split())
print(calendar.day_name[datetime.date(2009,m,d).weekday()])