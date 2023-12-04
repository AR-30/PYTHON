## calendar, date, inbuilt functions

import calendar
import datetime
import time
m=1
y=0
print(calendar.month(y,m))                      ## prints the calendar
print(datetime.datetime.now())                  ## prints current date and time
print(time.gmtime())                            ## prints date and time
print(time.localtime())                         ## same as above
print(type(datetime.datetime.now()))            ## o/p = datetime.datetime
print(type(calendar.month(y,m)))                ## o/p = str
print(type(calendar.monthcalendar(y,m)))        ## o/p = list
