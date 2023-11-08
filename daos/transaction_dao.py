from datetime import datetime
from contextlib import closing


class TransactionDao:
    def __init__(self, database):
        self.database = database

    def save_transaction(self, transaction, user_id):
        with closing(self.database.connect_to_database()) as connection:
            with connection.cursor() as cursor:
                amount = transaction['amount']
                transaction_type = 'credit' if amount > 0 else 'debit'
                date = transaction['date']

                current_year = datetime.now().year
                formatted_date = datetime.strptime(f"{date}/{current_year}", '%m/%d/%Y').strftime('%Y-%m-%d')
                cursor.execute("INSERT INTO transactions (amount, type, date) VALUES (%s, %s, %s)",
                               (amount, transaction_type, formatted_date))
                transaction_id = cursor.lastrowid

                cursor.execute("INSERT INTO user_transactions (user_id, transaction_id) VALUES (%s, %s)",
                               (user_id, transaction_id))

                connection.commit()
