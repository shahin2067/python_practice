even = list()
odd = list()
evenSum = 0
oddSum = 0
for i in range(0, 100):
    if(i % 2== 0):
        even.append(i)
        evenSum += i
    else:
        odd.append(i)
        oddSum += i
print("Even List:", even)
print("Odd List:", odd)

print("Even Sum:", evenSum)
print("Odd Sum:", oddSum)

evenLen = len(even)
print(evenLen)
print(len(odd))

print("Even Average:", evenSum / evenLen)
print("Odd Average:", oddSum / len(odd))