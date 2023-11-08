from flask import jsonify, request
from services.transaction_service import TransactionService
from utils import helper


def new_transaction():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    email = request.form['email']
    full_name = request.form['full_name']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and helper.allowed_file(file.filename):
        transaction_service = TransactionService()
        transactions = transaction_service.read_transactions(file)
        if not transactions:
            return jsonify({'error': 'Transactions could not be read'}), 400

        user = transaction_service.user_dao.get_or_create_user(email, full_name)
        summary = transaction_service.process_transactions(transactions, user)
        transaction_service.send_summary(summary, user)

        return jsonify(summary), 200
