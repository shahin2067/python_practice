even_number_list = []
s = 0
for i in range (0, 51):
    if i % 2 == 0:
        s += i
        even_number_list.append(i)
average = s / len(even_number_list)
print(even_number_list)
print(len(even_number_list))
print(s)
print(average)


# even_number_list = []
# s = 0
# i = 0
# while i <= 50:
#     if i % 2 == 0:
#         s += i
#         even_number_list.append(i)
#     i += 1
# average = s / len(even_number_list)
# print(even_number_list)
# print(len(even_number_list))
# print(s)
# print(average)