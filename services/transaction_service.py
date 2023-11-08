import csv
import io
from utils.helper import get_month_name
from services.email_service import EmailService
from config import env
from database.database import Database
from daos.user_dao import UserDao
from daos.transaction_dao import TransactionDao


class TransactionService:
    def __init__(self):
        self.db = Database()
        self.user_dao = UserDao(self.db)
        self.transaction_dao = TransactionDao(self.db)

    def read_transactions(self, file_storage):
        transactions = []
        try:
            file_stream = io.StringIO(file_storage.stream.read().decode('utf-8'), newline=None)
            reader = csv.DictReader(file_stream, delimiter=',')
            transactions = [
                {'date': row['date'], 'amount': float(row['transaction'])}
                for row in reader
            ]
        except ValueError as e:
            print(f"An invalid value was found in the CSV file: {e}")
        except Exception as e:
            print(f"An error occurred while processing the file: {e}")

        return transactions

    def process_transactions(self, transactions, user):
        summary = {
            'total_balance': 0,
            'transactions_per_month': {},
            'total_debit': 0,
            'total_credit': 0,
            'count_debit': 0,
            'count_credit': 0,
        }

        for transaction in transactions:
            amount = transaction['amount']
            summary['total_balance'] += amount

            month_key = transaction['date'][:1]
            summary['transactions_per_month'].setdefault(month_key, 0)
            summary['transactions_per_month'][month_key] += 1

            if amount < 0:
                summary['total_debit'] += amount
                summary['count_debit'] += 1
            else:
                summary['total_credit'] += amount
                summary['count_credit'] += 1

            self.transaction_dao.save_transaction(transaction, user['id'])

        summary['average_debit'] = summary['total_debit'] / summary['count_debit'] if summary['count_debit'] > 0 else 0
        summary['average_credit'] = summary['total_credit'] / summary['count_credit'] if summary['count_credit'] > 0 else 0

        return summary

    def send_summary(self, summary, user):
        html_content = f"""\
        <html>
        <head>
        </head>
        <body style="background-color: #f7f7f7; font-family: 'Arial', sans-serif; text-align: center; padding: 20px;">
            <div style="max-width: 600px; margin: auto; padding: 20px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 2px 3px rgba(0,0,0,0.1);">
                <img src="https://i.ibb.co/k4tRHC1/icon.png" alt="icon" style="width: 100px; height: auto; margin: 0 auto 20px; display: block;">
                <h2 style="color: #333333;">Account Summary</h2>
                <p style="color: #555555;">Hi {user['full_name']}!</p>
                <div style="background-color: #f2f2f2; padding: 15px; border-radius: 8px; margin: 15px 0;">
                    <p style="color: #333333; margin: 0;">Total balance is <strong>{summary['total_balance']}</strong></p>
                </div>
                {"<br>".join([f"<p style='margin: 0;'>Number of transactions in {get_month_name(month)}: <strong>{count}</strong></p>" for month, count in summary['transactions_per_month'].items()])}
                <p style="color: #333333;">Average debit amount: <strong>{round(summary['average_debit'], 2)}</strong></p>
                <p style="color: #333333;">Average credit amount: <strong>{round(summary['average_credit'], 2)}</strong></p>
            </div>
        </body>
        </html>
        """

        email_service = EmailService(env.SMTP_HOST, env.SMTP_PORT, env.SMTP_USER, env.SMTP_PASS)
        email_service.send_email(user['email'], "Account Summary", html_content)
