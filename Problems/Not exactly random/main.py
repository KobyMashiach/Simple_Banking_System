import random

# don't modify this code or variable `n` may not be available
n = int(input())

random.seed(n, 2)
n = random.randint(-100, 100)

print(n)
