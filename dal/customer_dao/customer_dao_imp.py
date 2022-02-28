from dal.customer_dao.customer_dao_interface import CustomerInterface
from entities.customer_class_information import Customer


class CustomerDAOImp(CustomerInterface):

    def __init__(self):
        pass

    def create_customer(self, customer: Customer) -> Customer:
        pass

    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass
