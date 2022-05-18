check = int(input())

if (check % 4 == 0 and check % 100 != 0) or check % 400 == 0:
    print("Leap")
else:
    print("Ordinary")
