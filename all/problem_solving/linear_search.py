a = [3, 4, 1, 41, 17, 21]
x = 34
c = 0

for i in range (0, len(a)):
    if a[i] == x:
        c+=1
        print("Found at location:", i)
        break
        
if c==0:
    print("not found")
