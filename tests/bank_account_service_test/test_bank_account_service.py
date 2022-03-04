from custom_exceptions.bad_input import BadInput
from custom_exceptions.negative_value_in_account import NegativeValueInAccount
from dal.bank_account_dao.bank_accont_dao_imp import BankAccountDAOImp
from service.bank_account_services.bank_account_services_imp import BankAccountServiceImp
from entities.bank_accont_class_information import BankAccount

service_bank = BankAccountServiceImp()


# service_create_account
def test_service_create_account_customer_id_is_int():
    try:
        test_data = BankAccount("2",0,200)
        result = service_bank.service_create_account(test_data)
        assert False
    except BadInput as e:
        assert str(e) == "Please enter a valid customer id"


def test_service_create_account_cash_amount_is_int():
    try:
        test_data = BankAccount(2, 0, "200")
        result = service_bank.service_create_account(test_data)
        assert False
    except BadInput as e:
        assert str(e) == "Please enter a valid cash amount"


def test_service_create_account_cash_amount_is_positive():
    try:
        test_data = BankAccount(2, 0, -200)
        result = service_bank.service_create_account(test_data)
        assert False
    except NegativeValueInAccount as e:
        assert str(e) == "Value cannot be negative, please enter positive integers"


# service_get_account_by_id
def test_service_get_account_by_id_bank_id_is_int():
    try:
        result = service_bank.service_get_account_by_id("one")
        assert False
    except BadInput as e:
        assert str(e) == "Wrong type of input entered"


# service_get_all_accounts_for_user
def test_service_get_all_accounts_for_user_customer_id_is_int():
    try:
        result = service_bank.service_get_all_accounts_for_user("one")
        assert False
    except BadInput as e:
        assert str(e) == "Wrong type of input entered"


# service_withdraw_from_account_by_id
def test_service_withdraw_from_account_by_id_bank_id_is_int():
    try:
        result = service_bank.service_withdraw_from_account_by_id("one",200)
        assert False
    except BadInput as e:
        assert str(e) == "Wrong type of input entered"


def test_service_withdraw_from_account_by_id_cash_amount_is_int():
    try:
        result = service_bank.service_withdraw_from_account_by_id(0, "200")
        assert False
    except BadInput as e:
        assert str(e) == "Wrong type of input entered"


def test_service_withdraw_from_account_by_id_cash_amount_is_positive():
    try:
        result = service_bank.service_withdraw_from_account_by_id(0, -200)
        assert False
    except NegativeValueInAccount as e:
        assert str(e) == "Value cannot be negative, please enter positive integers"


# service_deposit_into_account_by_id
def test__service_deposit_into_account_by_id_bank_id_is_int():
    try:
        result = service_bank.service_deposit_into_account_by_id("one", 200)
        assert False
    except BadInput as e:
        assert str(e) == "Wrong type of input entered"


def test_service_deposit_into_account_by_id_cash_amount_is_int():
    try:
        result = service_bank.service_deposit_into_account_by_id(0, "200")
        assert False
    except BadInput as e:
        assert str(e) == "Wrong type of input entered"


def test_service_deposit_into_account_by_id_cash_amount_is_positive():
    try:
        result = service_bank.service_deposit_into_account_by_id(0, -200)
        assert False
    except NegativeValueInAccount as e:
        assert str(e) == "Value cannot be negative, please enter positive integers"


# service_transfer_money_between_accounts_by_their_ids
def test__service_deposit_into_account_by_id_bank_id_1_is_int():
    try:
        result = service_bank.service_transfer_money_between_accounts_by_their_ids("one",0, 200)
        assert False
    except BadInput as e:
        assert str(e) == "Wrong type of input entered"


def test__service_deposit_into_account_by_id_bank_id_2_is_int():
    try:
        result = service_bank.service_transfer_money_between_accounts_by_their_ids(1, "0", 200)
        assert False
    except BadInput as e:
        assert str(e) == "Wrong type of input entered"


def test_service_deposit_into_account_by_id_cash_amount_is_int():
    try:
        result = service_bank.service_transfer_money_between_accounts_by_their_ids(1, 0, "200")
        assert False
    except BadInput as e:
        assert str(e) == "Wrong type of input entered"


def test_service_deposit_into_account_by_id_cash_amount_is_positive():
    try:
        result = service_bank.service_transfer_money_between_accounts_by_their_ids(1, 0, -200)
        assert False
    except NegativeValueInAccount as e:
        assert str(e) == "Value cannot be negative, please enter positive integers"


# service_delete_account_by_id
def test_service_delete_account_by_id_non_int_variable():
    try:
        result = service_bank.service_delete_account_by_id(1)
        assert False
    except BadInput as e:
        assert str(e) == "Wrong type of input entered"
