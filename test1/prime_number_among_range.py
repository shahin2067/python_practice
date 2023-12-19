prime_numbers = []
non_prime_numbers = []

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            non_prime_numbers.append(num)
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

print("Prime numbers between 1 and 100 are:")
print(prime_numbers)

print("\nNon-prime numbers between 1 and 100 are:")
print(non_prime_numbers)
