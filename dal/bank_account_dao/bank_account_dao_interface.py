from abc import ABC, abstractmethod

from entities.bank_accont_class_information import BankAccount


class BankAccountDAOInterface(ABC):

    @abstractmethod
    def create_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def get_account_by_id(self, account_search_id: int) -> BankAccount:
        pass

    @abstractmethod
    def get_all_accounts_for_user(self, customer_id: int) -> [BankAccount]:
        pass

    @abstractmethod
    def withdraw_from_account_by_id(self, account_id: int, withdraw_amount: int) -> BankAccount:
        pass

    @abstractmethod
    def deposit_into_account_by_id(self,  account_id: int, deposit_amount: int) -> BankAccount:
        pass

    @abstractmethod
    def transfer_money_between_accounts_by_their_ids(self, account_id_to_withdraw: int, account_id_to_deposit: int, transfer_amount: int) -> bool:
        pass

    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass
