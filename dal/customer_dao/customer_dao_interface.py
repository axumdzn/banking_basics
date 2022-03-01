from abc import ABC, abstractmethod

from entities.customer_class_information import Customer


class CustomerInterface(ABC):

    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def delete_customer_by_id(self, customer_delete_id: int) -> bool:
        pass
