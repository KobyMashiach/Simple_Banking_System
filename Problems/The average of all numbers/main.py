num1 = int(input())
num2 = int(input())

ava = 0
count = 0

for i in range(num1, num2 + 1, 1):
    if i % 3 == 0:
        count += 1
        ava += i

if count == 0:
    print(0)
else:
    print(ava / count)
