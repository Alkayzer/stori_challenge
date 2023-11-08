import pymysql
import os
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self):
        self.db_config = {
            'DB_HOST': os.getenv('DB_HOST'),
            'DB_USER': os.getenv('DB_USER'),
            'DB_PASS': os.getenv('DB_PASS'),
            'DB_NAME': os.getenv('DB_NAME'),
        }

    def connect_to_database(self):
        try:
            connection = pymysql.connect(
                host=self.db_config['DB_HOST'],
                user=self.db_config['DB_USER'],
                password=self.db_config['DB_PASS'],
                database=self.db_config['DB_NAME'],
                cursorclass=pymysql.cursors.DictCursor
            )
            return connection
        except pymysql.MySQLError as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
