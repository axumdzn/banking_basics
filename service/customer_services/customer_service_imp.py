from custom_exceptions.bad_input import BadInput
from dal.customer_dao.customer_dao_interface import CustomerInterface
from entities.customer_class_information import Customer
from service.customer_services.customer_service_interface import CustomerServiceInterface


class CustomerServiceImp(CustomerServiceInterface):

    def __init__(self, customer_list : CustomerInterface):
        self.customer_list = customer_list

    def service_create_customer(self, customer: Customer) -> Customer:
        if type(customer.first_name) != str:
            raise BadInput("Please enter a correct first name")
        elif type(customer.first_name) != str:
            raise BadInput("Please enter a correct last name")
        else:
            return self.customer_list.create_customer(customer)

    def service_delete_customer_by_id(self, customer_delete_id: int) -> bool:
        if type(customer_delete_id) != int:
            raise BadInput("Please enter a correct customer id number")
        else:
            return self.customer_list.delete_customer_by_id(customer_delete_id)
