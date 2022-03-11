from custom_exceptions.bad_input import BadInput
from custom_exceptions.name_too_long import NameTooLong
from dal.customer_dao.customer_dao_postgres import CustomerDaoPostgres
from service.customer_services.customer_service_postgres import CustomerServiceImpPostgres
from entities.customer_class_information import Customer


customer_dao = CustomerDaoPostgres()
customer_service = CustomerServiceImpPostgres(customer_dao)


# needs to test success for each method
def test_service_create_customer_success():
    test = Customer(0, "Bobby", "Flay")
    result = customer_service.service_create_customer(test)
    assert result.first_name == "Bobby"


# create customer
def test_service_create_customer_first_name_datatype():
    try:
        test = Customer(0, 1, "Smith")
        result = customer_service.service_create_customer(test)
        assert False
    except BadInput as e:
        assert str(e) == "Please enter a correct first name"


def test_service_create_customer_first_name_length():
    try:
        test = Customer(0, "askjldfaslkdjflskdjflaskjsdfsa", "Smith")
        result = customer_service.service_create_customer(test)
        assert False
    except NameTooLong as e:
        assert str(e) == "Please enter name with less than 20 characters"


def test_service_create_customer_last_name_datatype():
    try:
        test = Customer(0, "john", 2)
        result = customer_service.service_create_customer(test)
        assert False
    except BadInput as e:
        assert str(e) == "Please enter a correct last name"


def test_service_create_customer_last_name_length():
    try:
        test = Customer(0, "John", "askjldfaslkdjflskdjflaskjsdfsa")
        result = customer_service.service_create_customer(test)
        assert False
    except NameTooLong as e:
        assert str(e) == "Please enter name with less than 20 characters"


# service_delete_customer_by_id
def test_service_delete_customer_by_id_non_int():
    try:
        result = customer_service.service_delete_customer_by_id("2")
        assert False
    except BadInput as e:
        assert str(e) == "Please enter a correct customer id number"


def test_service_delete_customer_by_id_success():
    result = customer_service.service_delete_customer_by_id(1)
    assert result is True

