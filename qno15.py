s = "abc123"
letters = 0
digits = 0

for i in s:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)
