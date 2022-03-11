from flask import Flask, request, jsonify

from entities.bank_accont_class_information import BankAccount
from entities.customer_class_information import Customer
from service.bank_account_services.bank_account_services_postgres import BankAccountServiceImpPostgres
from service.customer_services.customer_service_postgres import CustomerServiceImpPostgres
from dal.customer_dao.customer_dao_postgres import CustomerDaoPostgres
from dal.bank_account_dao.bank_account_dao_postgres import BankAccountDaoPostgres


app: Flask = Flask(__name__)

# Assign my customer and bank stuff here
bank_dao = BankAccountDaoPostgres()
bank_service = BankAccountServiceImpPostgres(bank_dao)
customer_dao = CustomerDaoPostgres()
customer_service = CustomerServiceImpPostgres(customer_dao)


# I need to make routes for all the options aka the 8 options unless I'm asked for full crud functionality aka update
# customers first
@app.route("/api/customer/create_customer", methods=["POST"])
def api_create_customer():
    request_content: dict = request.get_json()
    global customer_service
    customer = Customer(request_content["customerId"], request_content["firstName"], request_content["lastName"])
    print(customer)
    result = customer_service.service_create_customer(customer)
    return f"Created a customer with id {result.customer_id}, first name: {result.first_name}: last name: {result.last_name}", 200


@app.route("/api/customer/delete_customer_by_id/<customer_id>", methods=["DELETE"])
def api_delete_customer_by_id(customer_id: str):
    customer = int(customer_id)
    result = customer_service.service_delete_customer_by_id(customer)
    return jsonify(result), 200


# bank account api calls
@app.route("/api/bank_account/create_account", methods=["POST"])
def api_create_account():
    account = request.get_json()
    result = bank_service.service_create_account(BankAccount(account["bankId"], account["balance"], account["customerId"]))
    return f"You created a new account with the id of {result.bank_id}", 201


@app.route("/api/bank_account/get_account_by_id/<account_id>", methods=["GET"])
def api_get_account_by_id(account_id: str):
    account_id = int(account_id)
    result = bank_service.service_get_account_by_id(account_id)
    new_result = {
        "bankId": result.bank_id,
        "balance": result.balance,
        "customerId": result.customer_id
    }
    return jsonify(new_result), 200


@app.route("/api/bank_account/get_all_accounts_for_user/<customer_id>", methods=["GET"])
def api_get_all_accounts_for_user(customer_id: str):
    customer_id = int(customer_id)
    result = bank_service.service_get_all_accounts_for_user(customer_id)
    new_result = []
    for account in result:
        temp = {
            "bankId": account.bank_id,
            "balance": account.balance,
            "customerId": account.customer_id
        }
        new_result.append(temp)
    return jsonify(new_result), 200


@app.route("/api/bank_account/withdraw_from_account_by_id", methods=["PUT"])
def api_withdraw_from_account_by_id():
    request_content = request.get_json()
    account_id = request_content["accountId"]
    withdraw_amount = request_content["withdrawAmount"]
    result = bank_service.service_withdraw_from_account_by_id(account_id, withdraw_amount)
    return f"New balance is {result.balance}", 200


@app.route("/api/bank_account/deposit_into_account_by_id", methods=["PUT"])
def api_deposit_into_account_by_id():
    request_content = request.get_json()
    account_id = request_content["accountId"]
    deposit_amount = request_content["depositAmount"]
    result = bank_service.service_deposit_into_account_by_id(account_id, deposit_amount)
    return f"New balance is {result.balance}", 201


@app.route("/api/bank_account/transfer_money_between_accounts_by_their_ids", methods=["PUT"])
def api_transfer_money_between_accounts_by_their_ids():
    request_content = request.get_json()
    account_id_to_withdraw = request_content["accountWithdraw"]
    account_id_to_deposit = request_content["accountDeposit"]
    transfer_amount = request_content["transferAmount"]
    result = bank_service.service_transfer_money_between_accounts_by_their_ids(account_id_to_withdraw, account_id_to_deposit, transfer_amount)
    return jsonify(result), 201


@app.route("/api/bank_account/delete_account_by_id/<account_id>", methods=["DELETE"])
def api_delete_account_by_id(account_id: str):
    account_id = int(account_id)
    result = bank_service.service_delete_account_by_id(account_id)
    return jsonify(result), 200


app.run()
