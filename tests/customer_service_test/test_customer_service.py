from custom_exceptions.bad_input import BadInput
from dal.customer_dao.customer_dao_imp import CustomerDAOImp
from service.customer_services.customer_service_imp import CustomerServiceImp
from entities.customer_class_information import Customer


customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)

# create customer
def test_service_create_customer_first_name_datatype():
    try:
        result = Customer(0, 1, "Smith")
        assert False
    except BadInput as e:
        assert str(e) == "Wrong datatype entered"


def test_service_create_customer_last_name_datatype():
    try:
        test = Customer(0, "john", 2)
        result = customer_service.service_create_customer(test)
        assert False
    except BadInput as e:
        assert str(e) == "Wrong datatype entered"


# service_delete_customer_by_id
def test_service_delete_customer_by_id_non_int():
    try:
        result = customer_service.service_delete_customer_by_id("2")
        assert False
    except BadInput as e:
        assert str(e) == "Wrong datatype entered"
