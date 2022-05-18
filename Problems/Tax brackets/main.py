income = int(input())

if 0 <= income <= 15527:
    percent = 0
elif 15528 <= income <= 42707:
    percent = 15
elif 42708 <= income <= 132406:
    percent = 25
else:
    percent = 28

print("The tax for {0} is {1}%. That is {2} dollars!".format(income, percent, int(round(income * percent * 0.01))))
