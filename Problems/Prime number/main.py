num = int(input())
check = True
if num <= 1:
    check = False
else:
    for i in range(2, num - 1):
        if num % i == 0:
            check = False
            break

if check:
    print("This number is prime")
else:
    print("This number is not prime")
