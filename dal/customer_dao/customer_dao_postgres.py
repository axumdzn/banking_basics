from custom_exceptions.id_not_found import IdNotFound
from dal.customer_dao.customer_dao_interface import CustomerInterface
from entities.customer_class_information import Customer
from util.manage_connection import connection


class CustomerDaoPostgres(CustomerInterface):

    def create_customer(self, customer: Customer) -> Customer:
        sql = "insert into customer values(default, %s, %s) returning customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name))
        connection.commit()
        customer.customer_id = cursor.fetchone()[0]
        return customer

    def delete_customer_by_id(self, customer_delete_id: int) -> bool:
        sql = "delete from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_delete_id])
        connection.commit()
        if cursor.rowcount != 0:
            return True
        else:
            raise IdNotFound("No customer matches this id given: please try again")
