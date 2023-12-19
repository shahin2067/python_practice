num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
i = 4

while i !=0:
    i = num1 % num2
    num1 = num2
    num2 = i
print(num2)