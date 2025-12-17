num = 153
temp = num
sum = 0
digits = len(str(num))

for _ in range(digits):
    rem = temp % 10
    sum += rem ** digits
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
