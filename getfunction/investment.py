class investment:
    def __init__(self,principal,rate,time):
        self.principal = principal
        self.rate = rate
        self.time = time
    def calculate_simple_interest(self):
        interest = (self.principal * self.rate * self.time) / 100
        return self.principal + interest
    def calculate_compound_interest(self):
        amount =   self.principal * (1 + self.rate) / 100 ** self.time
        return amount
    