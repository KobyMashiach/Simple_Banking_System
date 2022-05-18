string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

count = 0

for vowel in string:
    for letter in vowel:
        for i in vowels:
            if i == letter:
                count += 1

print(count)
