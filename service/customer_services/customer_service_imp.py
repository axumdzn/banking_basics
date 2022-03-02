from dal.customer_dao.customer_dao_interface import CustomerInterface
from entities.customer_class_information import Customer
from service.customer_services.customer_service_interface import CustomerServiceInterface


class CustomerServiceImp(CustomerServiceInterface):

    def __init__(self, customer_list : CustomerInterface):
        self.customer_list = customer_list

    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    def service_delete_customer_by_id(self, customer_delete_id: int) -> bool:
        pass
