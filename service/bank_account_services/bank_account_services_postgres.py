from custom_exceptions.bad_input import BadInput
from custom_exceptions.negative_value_in_account import NegativeValueInAccount
from dal.bank_account_dao.bank_account_dao_postgres import BankAccountDaoPostgres
from entities.bank_accont_class_information import BankAccount
from service.bank_account_services.bank_account_services_interface import BankAccountServiceInterface


class BankAccountServiceImpPostgres(BankAccountServiceInterface):

    def __init__(self, bank_account_dao: BankAccountDaoPostgres):
        self.bank_account_dao = bank_account_dao

    def service_create_account(self, bank_account: BankAccount) -> BankAccount:
        if type(bank_account.customer_id) != int:
            raise BadInput("Please enter a valid customer id")
        elif type(bank_account.balance) != int:
            raise BadInput("Please enter a valid cash amount")
        elif bank_account.balance < 0:
            raise NegativeValueInAccount("Value cannot be negative, please enter positive integers")
        else:
            return self.bank_account_dao.create_account(bank_account)

    def service_get_account_by_id(self, account_search_id: int) -> BankAccount:
        if type(account_search_id) != int:
            raise BadInput("Wrong type of input entered")
        else:
            return self.bank_account_dao.get_account_by_id(account_search_id)

    def service_get_all_accounts_for_user(self, customer_id: int) -> [BankAccount]:
        if type(customer_id) != int:
            raise BadInput("Wrong type of input entered")
        else:
            return self.bank_account_dao.get_all_accounts_for_user(customer_id)

    def service_withdraw_from_account_by_id(self, account_id: int, withdraw_amount: int) -> BankAccount:
        if type(account_id) != int:
            raise BadInput("Wrong type of input entered")
        elif type(withdraw_amount) != int:
            raise BadInput("Wrong type of input entered")
        elif withdraw_amount < 0:
            raise NegativeValueInAccount("Value cannot be negative, please enter positive integers")
        else:
            return self.bank_account_dao.withdraw_from_account_by_id(account_id, withdraw_amount)

    def service_deposit_into_account_by_id(self, account_id: int, deposit_amount: int) -> BankAccount:
        if type(account_id) != int:
            raise BadInput("Wrong type of input entered")
        elif type(deposit_amount) != int:
            raise BadInput("Wrong type of input entered")
        elif deposit_amount < 0:
            raise NegativeValueInAccount("Value cannot be negative, please enter positive integers")
        else:
            return self.bank_account_dao.deposit_into_account_by_id(account_id, deposit_amount)

    def service_transfer_money_between_accounts_by_their_ids(self, account_id_to_withdraw: int,
                                                             account_id_to_deposit: int, transfer_amount: int) -> bool:
        if type(account_id_to_deposit) != int:
            raise BadInput("Wrong type of input entered")
        elif type(account_id_to_withdraw) != int:
            raise BadInput("Wrong type of input entered")
        elif type(transfer_amount) != int:
            raise BadInput("Wrong type of input entered")
        elif transfer_amount < 0:
            raise NegativeValueInAccount("Value cannot be negative, please enter positive integers")
        else:
            return self.bank_account_dao.transfer_money_between_accounts_by_their_ids(account_id_to_withdraw,
                                                                                      account_id_to_deposit,
                                                                                      transfer_amount)

    def service_delete_account_by_id(self, account_id: int) -> bool:
        if type(account_id) != int:
            raise BadInput("Wrong type of input entered")
        else:
            return self.bank_account_dao.delete_account_by_id(account_id)
