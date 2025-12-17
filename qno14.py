lst = [1,2,3,4,"a","b"]
num = []
string = []

for i in lst:
    if type(i) == int:
        num.append(i)
    else:
        string.append(i)

print(num)
print(string)
