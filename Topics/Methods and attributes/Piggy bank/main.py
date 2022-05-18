class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = 1
        self.cents = 1

    def add_money(self, dollars, cents):
        if self.cents + cents < 100:
            self.cents += cents
        else:
            self.dollars += (self.cents + cents) // 100
            self.cents += cents
            self.cents %= 100
        self.dollars += dollars
