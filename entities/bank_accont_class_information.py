class BankAccount:

    def __init__(self, customer_id: int, bank_id: int, cash_amount: int):
        self.customer_id = customer_id
        self.bank_id = bank_id
        self.cash_amount = cash_amount


"""
Things that a bank account needs according to the rule set :
a unique id
customer id for the owner 
cash currently in the account
"""