import unittest
import bcrypt
from functions import (
    ValidationError,
    DigitsInPassword,
    LengthPassword,
    UpperLetterInPassword,
    LowerLetterInPassword,
    SpecialCharacterInPassword,
    LoginSimilarToPassword,
    LoginAndPasswordValidation,
)


class TestDigitsInPassword(unittest.TestCase):
    def test_enter_valid_password_with_digits(self):
        digits_validator = DigitsInPassword("password123")
        self.assertTrue(
            digits_validator.is_valid(), "Password with digits should be valid"
        )

    def test_enter_invalid_password_without_digits(self):
        digits_validation = DigitsInPassword("passwordwithoutdigits")
        with self.assertRaises(
            ValidationError, msg="Password without digits should raise an error"
        ):
            digits_validation.is_valid()

    def test_enter_invalid_empty_password(self):
        digits_validation = DigitsInPassword("")
        with self.assertRaises(
            ValidationError, msg="Password without text should raise an error"
        ):
            digits_validation.is_valid()


class TestLengthPassword(unittest.TestCase):
    def test_enter_valid_length_password(self):
        length_validator = LengthPassword("Morethantenwords")
        self.assertTrue(
            length_validator.is_valid(),
            "Password have more than 10 words - should be valid ",
        )

    def test_enter_invalid_length_password(self):
        length_validator = LengthPassword("Lessthan")
        with self.assertRaises(
            ValidationError, msg="Password is too short - should raise an error"
        ):
            length_validator.is_valid()

    def test_enter_invalid_empty_password(self):
        length_validator = LengthPassword("")
        with self.assertRaises(
            ValidationError, msg="Password without letters should raise an error"
        ):
            length_validator.is_valid()


class TestUpperLetterInPassword(unittest.TestCase):
    def test_enter_valid_password_with_upper_letter(self):
        upper_validator = UpperLetterInPassword("Passwordwithupperletter")
        self.assertTrue(
            upper_validator.is_valid(),
            "Password with at least one upper letters should be valid ",
        )

    def test_enter_invalid_password_without_upper_letter(self):
        upper_validator = UpperLetterInPassword("passwordwithoutupperletter")
        with self.assertRaises(
            ValidationError,
            msg="Password without any upper letters should raise an error",
        ):
            upper_validator.is_valid()

    def test_enter_invalid_password_with_only_upper_letter(self):
        upper_validator = UpperLetterInPassword("PASSWORD")
        self.assertTrue(
            upper_validator.is_valid(),
            "Password with all upper letters should be valid ",
        )

    def test_enter_invalid_password_without_any_letter(self):
        upper_validator = UpperLetterInPassword("1234567890")
        with self.assertRaises(
            ValidationError, msg="Password without any letters should raise an error"
        ):
            upper_validator.is_valid()

    def test_enter_invalid_password_with_all_lower_letters(self):
        upper_validator = UpperLetterInPassword("abcdefghijklmnopqrstuvwxyz")
        with self.assertRaises(
            ValidationError,
            msg="Password with all lower letters should raise an error ",
        ):
            upper_validator.is_valid()

    def test_enter_valid_password_with_digits_and_special_characters(self):
        upper_validator = UpperLetterInPassword("P@ssw0rdWithLower")
        self.assertTrue(
            upper_validator.is_valid(),
            "Password with digits and special characters should be valid",
        )

    def test_enter_invalid_password_empty_password(self):
        upper_validator = UpperLetterInPassword("")
        with self.assertRaises(
            ValidationError, msg="Password without letters should raise an error"
        ):
            upper_validator.is_valid()


class TestLowerLetterInPassword(unittest.TestCase):
    def test_enter_valid_password_with_lower_letter(self):
        lower_validator = LowerLetterInPassword("PASSWORDWITHLOWERletter")
        self.assertTrue(
            lower_validator.is_valid(),
            "Expected password with at least one lower letter to be valid",
        )

    def test_enter_invalid_password_without_lower_letter(self):
        lower_validator = LowerLetterInPassword("PASSWORDWITHOUTLOWERLETTER")
        with self.assertRaises(
            ValidationError,
            msg="Password without any lower letter should raise an error",
        ):
            lower_validator.is_valid()

    def test_enter_valid_password_with_only_lower_letter(self):
        lower_validator = LowerLetterInPassword("passwordwithlowerletter")
        self.assertTrue(
            lower_validator.is_valid(),
            "Password with only lower letter should be valid",
        )

    def test_enter_invalid_password_without_any_letter(self):
        lower_validator = LowerLetterInPassword("1234567890")
        with self.assertRaises(
            ValidationError, msg="Password without any letters should raise an error"
        ):
            lower_validator.is_valid()

    def test_enter_valid_password_with_all_lower_letters(self):
        lower_validator = LowerLetterInPassword("abcdefghijklmnopqrstuvwxyz")
        self.assertTrue(
            lower_validator.is_valid(),
            "Password with all lower letters should be valid ",
        )

    def test_enter_valid_password_with_digits_and_special_characters(self):
        lower_validator = LowerLetterInPassword("P@ssw0rdWithLower")
        self.assertTrue(
            lower_validator.is_valid(),
            "Password with digits and special characters should be valid",
        )

    def test_enter_invalid_password_empty_password(self):
        lower_validator = LowerLetterInPassword("")
        with self.assertRaises(
            ValidationError, msg="Password without letters should raise an error"
        ):
            lower_validator.is_valid()


class TestSpecialCharacterInPassword(unittest.TestCase):
    def test_enter_valid_password_with_special_character(self):
        special_character_validator = SpecialCharacterInPassword("PasswordWith@")
        self.assertTrue(
            special_character_validator.is_valid(),
            "Password with at least one special character should be valid",
        )

    def test_enter_invalid_password_without_special_character(self):
        special_character_validator = SpecialCharacterInPassword(
            "PASSWORDwithoutSPECIALcharacter"
        )
        with self.assertRaises(
            ValidationError,
            msg="Password without any special character should raise an error",
        ):
            special_character_validator.is_valid()

    def test_enter_valid_password_with_more_than_one_special_characters_and_digit(self):
        special_character_validator = SpecialCharacterInPassword(
            "P@ssw0rdWithLower!@#$"
        )
        self.assertTrue(
            special_character_validator.is_valid(),
            "Password with more than one special characters and digit should be valid",
        )

    def test_enter_invalid_password_empty_password(self):
        special_character_validator = SpecialCharacterInPassword("")
        with self.assertRaises(
            ValidationError, msg="Password without letters should raise an error"
        ):
            special_character_validator.is_valid()


class TestLoginSimilarToPassword(unittest.TestCase):
    def test_enter_invalid_login_is_same_as_password(self):
        login_similar_validator = LoginSimilarToPassword(
            "LoginIsSameAsPassword", "LoginIsSameAsPassword"
        )
        with self.assertRaises(
            ValidationError,
            msg="Login same as password, test should raise an error ",
        ):
            login_similar_validator.is_valid()

    def test_enter_invalid_login_is_very_similar_to_password(self):
        login_similar_validator = LoginSimilarToPassword(
            "LoginIsSimilarToPassword", "LoginIsSimilarTo@Password"
        )
        with self.assertRaises(
            ValidationError,
            msg="Login very similar to password should raise an error ",
        ):
            login_similar_validator.is_valid()

    def test_enter_valid_login_is_not_similar_to_password(self):
        login_similar_validator = LoginSimilarToPassword("Login", "Python3@")
        self.assertTrue(
            login_similar_validator.is_valid(),
            "Login is not similar to password should be valid",
        )


class TestLoginAndPasswordValidation(unittest.TestCase):
    def test_enter_valid_login_and_password(self):
        validator = LoginAndPasswordValidation("Login", "Password1234!")
        self.assertTrue(validator.is_valid(), "Login and password should be valid")

    def test_enter_invalid_password_without_special_character(self):
        validator = LoginAndPasswordValidation("Login", "password1234")
        self.assertFalse(
            validator.is_valid(),
            "Password without at least one special character should be invalid ",
        )

    def test_enter_invalid_length_password(self):
        validator = LoginAndPasswordValidation("Login", "password")
        self.assertFalse(validator.is_valid(), "Password is too short ")

    def test_enter_invalid_only_upper_letter(self):
        validator = LoginAndPasswordValidation("Login", "PASSWORD")
        self.assertFalse(
            validator.is_valid(),
            "Password doesn't have at least one lower letter should be invalid",
        )

    def test_enter_valid_hash_password(self):
        validator = LoginAndPasswordValidation("Login", "Password1234@")
        hashed_password = validator.hash_password()
        self.assertTrue(
            bcrypt.checkpw("Password1234@".encode("utf-8"), hashed_password)
        )
