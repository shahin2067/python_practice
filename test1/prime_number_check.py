# def checkPrimeNumber(num):
#     if num > 1:
#         for i in range (2, int(num/2)+1):
#             if (num % i) == 0:
#                 print(num, "is not a prime number")
#                 break
#         else:
#             print("Yes,", num, "is a prime number")
#     else:
#         print(num, "is not a prime number")

# number = int(input("Enter a number: "))
# checkPrimeNumber(number)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = []
non_prime_numbers = []

for num in range(2, 101):
    if is_prime(num):
        prime_numbers.append(num)
    else:
        non_prime_numbers.append(num)

print("Prime numbers between 1 and 100 are:")
print(prime_numbers)

print("\nNon-prime numbers between 1 and 100 are:")
print(non_prime_numbers)
