from flask import Blueprint
from controllers.transaction_controller import new_transaction

transaction_bp = Blueprint('transaction_bp', __name__)

transaction_bp.route('/transaction', methods=['POST'])(new_transaction)
