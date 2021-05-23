from datetime import date, time, datetime, timedelta
#from datetime import time
#from datetime import datetime
#from datetime import timedelta

print(timedelta(days = 365, hours = 5, minutes = 1))

#print today's date
now = datetime.now()
print("today is: " + str(now))

#print today's date one year from now
print("One year from now it will be: " + str(now + timedelta(days = 365)))

#create timedelta which uses more than one argument
print("In 2 days and 3 weeks it will be:" +
      str(now + timedelta(days = 2, weeks =3)))

#calculate the day one week ago, formatted as a string
t = datetime.now() - timedelta(weeks = 1)
s = t.strftime("%A %B %d, %Y")

print("one week ago it was: " + s)

#How many days until next April Fool's day
today = date.today()
afd = date(today.year, 4, 1)

if afd < today:
    print("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year = today.year + 1)

#calculate next April's fools day
time_to_afd =afd - today
print("It's just", time_to_afd.days, "days until April Fool's Day")
