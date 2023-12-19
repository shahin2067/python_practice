myList = [10, "orange", 12, 11, "fish"]

### Access
# print(myList[3])
# for i in myList:
#     print(i)
# for j in range(len(myList)):
#     print(myList[j])
# print(myList[-1])
# print(myList[1:3])

### Insert
myList.insert(1, "student")
# print(myList)
myList.append(24)
print(myList)

### Update
print("before update:", myList)
myList[0] = "cow"
print("after update:", myList)


### Delete
myList.pop(0)
print(myList)
myList.remove(11)
print(myList)


