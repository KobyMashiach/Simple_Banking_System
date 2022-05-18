import random
import sqlite3

conn = sqlite3.connect("card.s3db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS card (id INT, number TEXT, pin TEXT, balance INT);")


class Card:
    def __init__(self):
        self.card_number_ls = []
        self.pin_code_ls = []

    def card_number(self):
        card_num = "400000" + str(random.randint(000000000, 999999999)).zfill(9)
        temp = []
        temp[:] = card_num
        digits_sum = 0
        count = 0
        for i in range(8):
            temp[count] = int(temp[count])
            temp[count] *= 2
            if temp[count] > 9:
                temp[count] -= 9
            count += 2

        for i in temp:
            digits_sum += int(i)

        digits_sum %= 10
        if digits_sum != 0:
            digits_sum = 10 - digits_sum
        digits_sum = str(digits_sum)
        card_num += str(digits_sum)
        self.card_number_ls.append(card_num)

        pin_code = random.randint(0000, 9999)
        pin_code = str(pin_code).zfill(4)
        self.pin_code_ls.append(pin_code)

        cur.execute("INSERT INTO card VALUES(11, {0}, {1}, 0);".format(card_num, pin_code))
        conn.commit()

        print("\nYour card has been created\nYour card number:\n{0}\nYour card PIN:\n{1}\n".format(card_num, pin_code))

    def log_in(self):
        print("\nEnter your card number:")
        card_num = input()
        print("Enter your PIN:")
        pin_code = input()
        check = False
        for i in self.card_number_ls:
            if i == card_num:
                if self.pin_code_ls[self.card_number_ls.index(card_num)] == pin_code:
                    check = True
                    print("\nYou have successfully logged in!\n")
                    while True:
                        print("1. Balance\n2. Log out\n0. Exit")
                        inp = input()
                        if inp == '1':
                            print("Balance: 0")
                        elif inp == '2':
                            print("\nYou have successfully logged out!\n")
                            break
                        elif inp == '0':
                            exit()
        if not check:
            print("Wrong card number or PIN!")


customer = Card()
while True:
    print("1. Create an account\n2. Log into account\n0. Exit")
    user = input()
    if user == '1':
        Card.card_number(customer)
    elif user == '2':
        Card.log_in(customer)
    elif user == '0':
        print("Bye!")
        exit()
