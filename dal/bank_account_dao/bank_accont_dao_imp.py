from custom_exceptions.negative_value_in_account import NegativeValueInAccount
from dal.bank_account_dao.bank_account_dao_interface import BankAccountDAOInterface
from entities.bank_accont_class_information import BankAccount


class BankAccountDAOImp(BankAccountDAOInterface):

    def create_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    def get_account_by_id(self, account_id: int) -> BankAccount:
        pass

    def get_all_accounts_for_user(self, customer_id: int) -> [BankAccount]:
        pass

    def withdraw_from_account_by_id(self, account_id: int, withdraw_amount: int) -> BankAccount:
        pass

    def deposit_into_account_by_id(self, account_id: int, deposit_amount: int) -> BankAccount:
        pass

    def transfer_money_between_accounts_by_their_ids(self, account_id_to_withdraw: int, account_id_to_deposit: int,
                                                     transfer_amount: int) -> bool:
        pass

    def delete_account_by_id(self, account_id: int) -> bool:
        pass