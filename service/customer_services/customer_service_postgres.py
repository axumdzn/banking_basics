from custom_exceptions.bad_input import BadInput
from custom_exceptions.name_too_long import NameTooLong
from dal.customer_dao.customer_dao_postgres import CustomerDaoPostgres
from entities.customer_class_information import Customer
from service.customer_services.customer_service_interface import CustomerServiceInterface


class CustomerServiceImpPostgres(CustomerServiceInterface):

    def __init__(self, customer_list: CustomerDaoPostgres):
        self.customer_list = customer_list

    def service_create_customer(self, customer: Customer) -> Customer:
        if type(customer.first_name) != str:
            raise BadInput("Please enter a correct first name")
        elif type(customer.last_name) != str:
            raise BadInput("Please enter a correct last name")
        elif len(customer.first_name) > 20:
            raise NameTooLong("Please enter name with less than 20 characters")
        elif len(customer.last_name) > 20:
            raise NameTooLong("Please enter name with less than 20 characters")
        else:
            return self.customer_list.create_customer(customer)

    def service_delete_customer_by_id(self, customer_delete_id: int) -> bool:
        if type(customer_delete_id) != int:
            raise BadInput("Please enter a correct customer id number")
        else:
            return self.customer_list.delete_customer_by_id(customer_delete_id)
