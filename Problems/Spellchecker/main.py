dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
user = input()
check = False
for value in dictionary:
    if user == value:
        check = True
        print("Correct")

if not check:
    print("Incorrect")
