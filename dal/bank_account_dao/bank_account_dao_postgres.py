from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.negative_value_in_account import NegativeValueInAccount
from dal.bank_account_dao.bank_account_dao_interface import BankAccountDAOInterface
from entities.bank_accont_class_information import BankAccount
from util.manage_connection import connection


class BankAccountDaoPostgres(BankAccountDAOInterface):
    def create_account(self, bank_account: BankAccount) -> BankAccount:
        sql = "insert into bank_account(default, %s, %s) returning bank_id"
        cursor = connection.cursor()
        cursor.execute(sql, (bank_account.cash_amount, bank_account.customer_id))
        connection.commit()
        bank_account.bank_id = cursor.fetchone()[0]
        return bank_account

    def get_account_by_id(self, account_search_id: int) -> BankAccount:
        sql = "select * from bank_account where bank_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_search_id])
        bank_record = cursor.fetchone()
        connection.commit()
        if bank_record is None:
            raise IdNotFound("An account with this id does not exist: please try again")
        else:
            return bank_record

    def get_all_accounts_for_user(self, customer_id: int) -> [BankAccount]:
        sql = "select * from bank_account where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        bank_record = cursor.fetchall()
        connection.commit()
        bank_list = []
        if len(bank_record) is 0:
            raise IdNotFound("An account with this id does not exist: please try again")
        else:
            for bank in bank_record:
                bank_list.append(BankAccount(bank))
            return bank_list

    def withdraw_from_account_by_id(self, account_id: int, withdraw_amount: int) -> BankAccount:
        sql = "select * from bank_account where bank_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        bank_record = cursor.fetchone()
        if bank_record is None:
            raise IdNotFound("An account with this id does not exist: please try again")
        elif bank_record.cash_amount > withdraw_amount:
            raise NegativeValueInAccount("Took too much money, negative values not allowed")
        else:
            bank_record.cash_amount -= withdraw_amount
        connection.commit()


    def deposit_into_account_by_id(self, account_id: int, deposit_amount: int) -> BankAccount:
        pass

    def transfer_money_between_accounts_by_their_ids(self, account_id_to_withdraw: int, account_id_to_deposit: int,
                                                     transfer_amount: int) -> bool:
        pass

    def delete_account_by_id(self, account_id: int) -> bool:
        pass