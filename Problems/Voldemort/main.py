import random


# work with this variable
n = int(input())
random.seed(n, 2)
string = "Voldemort"
n = random.choice(string)

print(n)
