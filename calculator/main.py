from calculator import Calculator
from prime_number_checker import PrimeNumberChecker
from check_leap_year import CheckLeapYear

print("Which calculator do you want to use -\n" 
            "1. Simple Calculator\n"
            "2. Check Leap Year\n"
            "3. Check Prime Number\n"
            )

select = int(input("Select operations form 1 or 2 or 3: "))

if select == 1:
    calculator = Calculator()
    print("Please select operation -\n" 
            "1. Add\n" \
            "2. Subtract\n" \
            "3. Multiply\n" \
            "4. Divide\n")

    operation = int(input("Select operations from 1 to 4: "))
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

    if operation == 1:
        print(number_1, "+", number_2, "=", calculator.add(number_1, number_2))
    elif operation == 2:
        print(number_1, "-", number_2, "=", calculator.subtract(number_1, number_2))
    elif operation == 3:
        print(number_1, "*", number_2, "=", calculator.multiply(number_1, number_2))
    elif operation == 4:
        print(number_1, "/", number_2, "=", calculator.divide(number_1, number_2))
    else:
        print("Invalid input")

elif select == 2:
    leap_year_checker = CheckLeapYear()
    leap_year_checker.check_leap_year()
elif select == 3:
    checkPrimeNumber = PrimeNumberChecker()
    checkPrimeNumber.primeNumber()

else:
    print("Invalid Input")
