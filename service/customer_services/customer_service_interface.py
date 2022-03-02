from abc import abstractmethod, ABC

from entities.customer_class_information import Customer


class CustomerServiceInterface(ABC):

    @abstractmethod
    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_delete_customer_by_id(self, customer_delete_id: int) -> bool:
        pass
