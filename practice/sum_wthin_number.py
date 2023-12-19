n = int(input("Enter The range of number: "))
sum = 0

# for i in range(1, n+1):
#     sum += i

i = 1
while (i <= n):
    sum += i
    i=i+1

print("1 to",n, "sum is =",sum)