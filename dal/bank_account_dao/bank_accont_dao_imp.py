from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.negative_value_in_account import NegativeValueInAccount
from dal.bank_account_dao.bank_account_dao_interface import BankAccountDAOInterface
from entities.bank_accont_class_information import BankAccount


class BankAccountDAOImp(BankAccountDAOInterface):

    def __init__(self):
        self.bank_account_list = []
        self.bank_account_id_increment = 0

    def create_account(self, bank_account: BankAccount) -> BankAccount:
        bank_account.bank_id = self.bank_account_id_increment
        self.bank_account_id_increment += 1
        self.bank_account_list.append(bank_account)
        return bank_account

    def get_account_by_id(self, account_search_id: int) -> BankAccount:
        for bank_account in self.bank_account_list:
            if bank_account.bank_id == account_search_id:
                return bank_account
        raise IdNotFound("An account with this id does not exist: please try again")

    def get_all_accounts_for_user(self, customer_id: int) -> [BankAccount]:
        user_accounts = []
        for bank_account in self.bank_account_list:
            if customer_id == bank_account.customer_id:
                user_accounts.append(bank_account)
        if len(user_accounts) > 0:
            return user_accounts
        else:
            raise IdNotFound("An account with this id does not exist: please try again")

    def withdraw_from_account_by_id(self, account_id: int, withdraw_amount: int) -> BankAccount:
        for bank_account in self.bank_account_list:
            if bank_account.bank_id == account_id:
                if bank_account.balance - withdraw_amount < 0:
                    raise NegativeValueInAccount("Took too much money, negative values not allowed")
                else:
                    bank_account.balance -= withdraw_amount
                    return bank_account
        raise IdNotFound("An account with this id does not exist: please try again")

    def deposit_into_account_by_id(self, account_id: int, deposit_amount: int) -> BankAccount:
        for bank_account in self.bank_account_list:
            if bank_account.bank_id == account_id:
                bank_account.balance += deposit_amount
                return bank_account
        raise IdNotFound("An account with this id does not exist: please try again")

    def transfer_money_between_accounts_by_their_ids(self, account_id_to_withdraw: int, account_id_to_deposit: int,
                                                     transfer_amount: int) -> bool:
        withdraw_account = BankAccount(0, 0, 100)
        deposit_account = BankAccount(0, 0, 100)
        for bank_account in self.bank_account_list:
            if account_id_to_deposit == bank_account.bank_id:
                deposit_account = bank_account
            elif account_id_to_withdraw == bank_account.bank_id:
                withdraw_account = bank_account
        if withdraw_account.bank_id == account_id_to_withdraw and deposit_account.bank_id == account_id_to_deposit:
            if withdraw_account.balance - transfer_amount < 0:
                raise NegativeValueInAccount("Took too much money, negative values not allowed")
            else:
                withdraw_account.balance -= transfer_amount
                deposit_account.balance += transfer_amount
                return True
        else:
            raise IdNotFound("An account with this id does not exist: please try again")

    def delete_account_by_id(self, account_id: int) -> bool:
        for bank_account in self.bank_account_list:
            if account_id == bank_account.bank_id:
                self.bank_account_list.remove(bank_account)
                return True
        raise IdNotFound("An account with this id does not exist: please try again")
