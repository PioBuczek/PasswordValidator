import unittest
import bcrypt
from database import PasswordDatabase
from unittest.mock import MagicMock, patch


class TestPasswordDatabase(unittest.TestCase):
    # The test checks if 'create_table_if_not_exists' method correctly creates a table in
    # the database if such a tabel does not exist.

    def test_create_table_if_not_exists(self):
        mock_connection = MagicMock()
        with patch("psycopg2.connect", return_value=mock_connection):
            with PasswordDatabase(
                "dbname", "user", "password", "host", "port"
            ) as password_db:
                mock_connection.cursor.assert_called_once()

    def test_save_password_and_login_if_is_valid(self):
        # The test checks whether the 'save_password_and_login_if_is_valid'
        # method correctly saves the given login data to the database.
        login = "test_login"
        password = "test_password"
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        mock_connection = MagicMock()
        with patch("psycopg2.connect", return_value=mock_connection):
            with PasswordDatabase(
                "dbname", "user", "password", "host", "port"
            ) as password_db:
                password_db.save_password_and_login_if_is_valid(login, password)
