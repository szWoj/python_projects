from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = date.today()
    print("Today date is ", today)
    print("Date components: ", today.day, today.month, today.year)
    print("Today weekday # is: ", today.weekday())

    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    print("Which is a: ", days[today.weekday()])

    #Formating time and date output
    now = datetime.now()
    print(now.strftime("The current year is: %Y"))
    #               weekday, day month year
    print(now.strftime("%a, %d, %B, %y"))
    #           12h format/ Minutes /Sec /PM(AM)
    print(now.strftime("%I:%M:%S %p"))
    #           24h format/ Minutes/ Seconds
    print(now.strftime("%H:%M:%S"))

    #Datetime objects
    #Get today's date from datetime class
    print("The current date and time is: ", now)

    #Get the current time
    t = datetime.time(now) #same as t = datetime.time(datetime.now())
    print(t)

if __name__ == "__main__":
    main()
