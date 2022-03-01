from custom_exceptions.id_not_found import IdNotFound
from dal.customer_dao.customer_dao_interface import CustomerInterface
from entities.customer_class_information import Customer


class CustomerDAOImp(CustomerInterface):
    customer_list = []
    id_incrementer = 0

    def create_customer(self, customer: Customer) -> Customer:
        customer.customer_id = self.id_incrementer
        self.id_incrementer += 1
        self.customer_list.append(customer)
        return customer

    def delete_customer_by_id(self, customer_delete_id: int) -> bool:
        for customer in self.customer_list:
            if customer.customer_id == customer_delete_id:
                self.customer_list.remove(customer)
                return True
        raise IdNotFound("No customer matches this id given: please try again")

