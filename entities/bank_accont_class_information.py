class BankAccount:

    def __init__(self, bank_id: int, balance: int, customer_id: int):
        self.customer_id = customer_id
        self.bank_id = bank_id
        self.balance = balance


"""
Things that a bank account needs according to the rule set :
a unique id
customer id for the owner 
cash currently in the account
"""