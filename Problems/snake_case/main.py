string = input()
for i in string:
    if 'A' <= i <= 'Z':
        index = string.index(i)
        if index == 0:
            string = string[:index] + i.lower() + string[index + 1:]
        else:
            string = string[:index] + "_" + i.lower() + string[index + 1:]

print(string)
