from dal.bank_account_dao.bank_accont_dao_imp import BankAccountDAOImp
from entities.bank_accont_class_information import BankAccount
from service.bank_account_services.bank_account_services_interface import BankAccountServiceInterface


class BankAccountServiceImp(BankAccountServiceInterface):

    def __init__(self, bank_account: BankAccount):
        pass


    def service_create_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    def service_get_account_by_id(self, account_search_id: int) -> BankAccount:
        pass

    def service_get_all_accounts_for_user(self, customer_id: int) -> [BankAccount]:
        pass

    def service_withdraw_from_account_by_id(self, account_id: int, withdraw_amount: int) -> BankAccount:
        pass

    def service_deposit_into_account_by_id(self, account_id: int, deposit_amount: int) -> BankAccount:
        pass

    def service_transfer_money_between_accounts_by_their_ids(self, account_id_to_withdraw: int,
                                                             account_id_to_deposit: int, transfer_amount: int) -> bool:
        pass

    def service_delete_account_by_id(self, account_id: int) -> bool:
        pass
