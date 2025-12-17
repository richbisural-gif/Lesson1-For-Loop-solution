list1 = [10, 2.5, "hello", True]
list2 = []

for item in list1:
    list2.append(type(item))

print(list2)