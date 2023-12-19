def check_leap_yaer(year):
    if(year % 400 == 0):
        print("Leap year")
    elif (year % 4 == 0) and (year % 100 != 0):
        print("Leap year")
    else:
        print("not leap year")

check_leap_yaer(2000)