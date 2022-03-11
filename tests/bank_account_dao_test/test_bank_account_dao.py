from custom_exceptions.id_not_found import IdNotFound
from dal.bank_account_dao.bank_account_dao_postgres import BankAccountDaoPostgres
from entities.bank_accont_class_information import BankAccount
from custom_exceptions.negative_value_in_account import NegativeValueInAccount

bank_account = BankAccountDaoPostgres()
# create_account tests


def test_create_account_success():
    test_value = BankAccount(0, 200, 1)
    result = bank_account.create_account(test_value)
    assert result.bank_id == 1


def test_create_account_unique_id():
    test_value = BankAccount(1, 300, 1)
    result = bank_account.create_account(test_value)
    assert result.bank_id != 1


# get_account_by_id tests


def test_get_account_by_id_success():
    result = bank_account.get_account_by_id(1)
    print(result)
    assert result.bank_id == 1


def test_get_account_by_id_with_nonexistent_id():
    try:
        result = bank_account.get_account_by_id(4)
        assert False
    except IdNotFound as e:
        assert str(e) == "An account with this id does not exist: please try again"


# get_all_accounts_for_user tests
def test_get_all_accounts_for_user_success():
    result = bank_account.get_all_accounts_for_user(1)
    assert result[0].customer_id == 1


def test_get_all_accounts_for_user_nonexistent_id():
    try:
        result = bank_account.get_all_accounts_for_user(4)
        assert False
    except IdNotFound as e:
        assert str(e) == "An account with this id does not exist: please try again"


# withdraw_from_account_by_id
def test_withdraw_from_account_by_id_success():
    result = bank_account.withdraw_from_account_by_id(1, 150)
    assert result.balance == 50


def test_withdraw_from_account_by_id_negative_value():
    try:
        result = bank_account.withdraw_from_account_by_id(1, 100)
        assert False
    except NegativeValueInAccount as e:
        assert str(e) == "Took too much money, negative values not allowed"


def test_withdraw_from_account_by_id_non_existent_id():
    try:
        result = bank_account.withdraw_from_account_by_id(0, 1000)
        assert False
    except IdNotFound as e:
        assert str(e) == "An account with this id does not exist: please try again"


# deposit_from_account_by_id
def test_deposit_into_account_by_id_success():
    result = bank_account.deposit_into_account_by_id(1, 150)
    assert result.balance == 200


def test_deposit_into_account_by_id_non_existent_id():
    try:
        result = bank_account.deposit_into_account_by_id(4, 1000)
        assert False
    except IdNotFound as e:
        assert str(e) == "An account with this id does not exist: please try again"


# transfer_money_between_accounts_by_their_ids
def test_transfer_from_account_by_id_success():
    result = bank_account.transfer_money_between_accounts_by_their_ids(1, 2, 100)
    assert result is True


def test_transfer_from_account_by_id_negative_value():
    try:
        result = bank_account.transfer_money_between_accounts_by_their_ids(1, 2, 150)
        assert result is False
    except NegativeValueInAccount as e:
        assert str(e) == "Took too much money, negative values not allowed"


def test_transfer_from_account_by_id_non_existent_id():
    try:
        result = bank_account.transfer_money_between_accounts_by_their_ids(0, 4, 1000)
        assert False
    except IdNotFound as e:
        assert str(e) == "An account with this id does not exist: please try again"


def test_delete_account_by_id_success():
    result = bank_account.delete_account_by_id(1)
    assert result is True


def test_delete_account_by_id_non_existing_account():
    try:
        result = bank_account.delete_account_by_id(1)
        assert False
    except IdNotFound as e:
        assert str(e) == "An account with this id does not exist: please try again"
