class CheckLeapYear:
    def check_leap_year(self):
        year = int(input("Enter year: "))
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))



# class CheckLeapYear:
#     year = int(input("Enter year: "))

#     if (year % 400 == 0) and (year % 100 == 0):
#         print("{0} is a leap year".format(year))

#     elif (year % 4 == 0) and (year % 100 != 0):
#         print("{0} is a leap year".format(year))

#     else:
#         print("{0} is not a leap year".format(year))

