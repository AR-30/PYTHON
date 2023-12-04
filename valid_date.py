## calendar, date, inbuilt functions

import calendar
import sys

d,m,y=map(int,input("Enter date in format dd/mm/yyyy : ").split('/'))
if(m<1 and m>12):
    sys.exit()
elif len(str(y))!=4:
    sys.exit()
else:
    l=calendar.monthcalendar(y,m)
    l1=l[len(l)-1]
    z=max(l1)
    if d>0 and d<=z:
        print("Valid date")
    else:
        print("invalid")
