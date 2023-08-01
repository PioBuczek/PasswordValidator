import psycopg2
import bcrypt


# I have created a Context Manager, which is used to create a PostgreSQL database.
# First, I create database with three columns: id, login, password.
# If password meets all the requirements, login and encrypted password will be added to the database.
class PasswordDatabase:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )
        self.create_table_if_not_exists()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

    def create_table_if_not_exists(self):
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
CREATE TABLE IF NOT EXISTS password_database (
    id SERIAL PRIMARY KEY,
    login text,
    password text
)
"""
                )

    def save_password_and_login_if_is_valid(self, login, password):
        with self.connection:
            with self.connection.cursor() as cursor:
                hashed_password = bcrypt.hashpw(
                    password.encode("utf-8"), bcrypt.gensalt()
                )

                cursor.execute(
                    "INSERT INTO password_database (login, password) VALUES (%s, %s);",
                    (login, hashed_password),
                )

        return True
