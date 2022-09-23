import random
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        for i in range(13):
            if i == 0:
                