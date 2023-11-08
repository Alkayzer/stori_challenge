from contextlib import closing


class UserDao:
    def __init__(self, database):
        self.database = database

    def get_or_create_user(self, email, full_name):
        with closing(self.database.connect_to_database()) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
                user = cursor.fetchone()

                if not user:
                    cursor.execute("INSERT INTO users (full_name, email) VALUES (%s, %s)", (full_name, email))
                    connection.commit()
                    user_id = cursor.lastrowid

                    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
                    user = cursor.fetchone()

                return user

