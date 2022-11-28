#Create a python program that outputs the specific day of the week 
# given a particular date.
import calendar
from datetime import datetime
'''year = 1995
month = 6
print (calendar.month(year,12))
print (calendar.calendar(year))'''

given_date = datetime(2020,11,6)
weekday= calendar.day_name[given_date.weekday()] #week () returns the week day number(0 is Monday) of the date specified in its arguments
print (weekday)

print (given_date.strftime('%A'))