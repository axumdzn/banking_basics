from custom_exceptions.id_not_found import IdNotFound
from dal.customer_dao.customer_dao_imp import CustomerDAOImp
from entities.customer_class_information import Customer

customer_dao = CustomerDAOImp()


def test_create_customer_success():
    test_customer = Customer(0, "Bob", "Smith")
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id == 0


def test_unique_id():
    test_customer = Customer(0, "John", "Cena")
    result = customer_dao.create_customer(test_customer)
    assert result != 0


# test delete


def test_delete_by_id_success():
    result = customer_dao.delete_customer_by_id(0)
    assert result is True


def test_delete_deleted_data():
    try:
        result = customer_dao.delete_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches this id given: please try again"
