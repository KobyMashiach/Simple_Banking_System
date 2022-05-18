word = input()

index1 = 0
index2 = len(word) - 1
check = True

for __i__ in range(0, len(word)):
    if word[index1] != word[index2]:
        check = False
        break
    index1 += 1
    index2 -= 1
    if index1 >= index2:
        break


if check:
    print("Palindrome")
else:
    print("Not palindrome")
