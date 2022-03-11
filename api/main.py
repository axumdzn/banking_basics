from flask import Flask, request, jsonify
from service.bank_account_services.bank_account_services_imp import BankAccountServiceImp
from service.customer_services.customer_service_imp import CustomerServiceImp


app: Flask = Flask(__name__)

# Assign my customer and bank stuff here
bank_service = BankAccountServiceImp
customer_service = CustomerServiceImp


# I need to make routes for all the options aka the 8 options unless I'm asked for full crud functionality aka update
# customers first
@app.route("/api/customer/create_customer", methods=["POST"])
def api_create_customer():
    request_content = request.get_json()
    global customer_service
    result = customer_service.service_create_customer(request_content)
    return jsonify(result), 200


@app.route("/api/customer/delete_customer_by_id/<customer_id>", methods=["DELETE"])
def api_delete_customer_by_id(customer_id: str):
    customer = int(customer_id)
    result = customer_service.service_delete_customer_by_id(customer)
    return jsonify(result), 200


# bank account api calls
@app.route("/api/bank_account/create_account", methods=["POST"])
def api_create_account():
    account = request.get_json()
    result = bank_service.service_create_account(account)
    return jsonify(result), 201


@app.route("/api/bank_account/get_account_by_id/<account_id>", methods=["GET"])
def api_get_account_by_id(account_id: str):
    account_id = int(account_id)
    result = bank_service.service_get_account_by_id(account_id)
    return jsonify(result), 200


@app.route("/api/bank_account/get_all_accounts_for_user/<customer_id>", methods=["GET"])
def api_get_all_accounts_for_user(customer_id: str):
    customer_id = int(customer_id)
    result = bank_service.service_get_all_accounts_for_user(customer_id)
    return jsonify(result), 200


@app.route("/api/bank_account/withdraw_from_account_by_id", methods=["PUT"])
def api_withdraw_from_account_by_id():
    request_content = request.get_json()
    request_content.account_id = int(request_content.account_id)
    request_content.withdraw_amount = int(request_content.withdraw_amount)
    result = bank_service.service_withdraw_from_account_by_id(request_content)
    return jsonify(result), 200


@app.route("/api/bank_account/deposit_into_account_by_id", methods=["PUT"])
def api_deposit_into_account_by_id():
    request_content = request.get_json()
    request_content.account_id = int(request_content.account_id)
    request_content.deposit_amount = int(request_content.withdraw_amount)
    result = bank_service.service_deposit_into_account_by_id(request_content)
    return jsonify(result), 201


@app.route("/api/bank_account/transfer_money_between_accounts_by_their_ids", methods=["PUT"])
def api_transfer_money_between_accounts_by_their_ids():
    request_content = request.get_json()
    request_content.account_id_to_withdraw = int(request_content.account_id_to_withdraw)
    request_content.account_id_to_deposit = int(request_content.account_id_to_deposit)
    request_content.transfer_amount = int(request_content.transfer_amount)
    result = bank_service.service_transfer_money_between_accounts_by_their_ids(request_content)
    return jsonify(result), 201


@app.route("/api/bank_account/delete_account_by_id/<account_id>", methods=["DELETE"])
def api_delete_account_by_id(account_id: str):
    account_id = int(account_id)
    result = bank_service.service_delete_account_by_id(account_id)
    return jsonify(result), 200


app.run()
