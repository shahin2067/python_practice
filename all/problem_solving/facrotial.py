number = int(input("Enter the number: "))
fac = 1

while(number != 0):
    fac *= number
    number -= 1
print(fac)