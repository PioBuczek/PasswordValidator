from abc import ABC, abstractmethod
from fuzzywuzzy import fuzz
import bcrypt


# I created class inheritance to Exception, because Exception used to report password validation errors.
# It is occurrence indicates that the password does not meet the requirements specified by one of the validators.
class ValidationError(Exception):
    pass


# I created abstract class because I want enforce certain structure to my application.
class AbstractClass(ABC):
    @abstractmethod
    def __init__(self, password):
        pass

    @abstractmethod
    def is_valid(self):
        pass


# I check that password has at least one digit
class DigitsInPassword(ABC):
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        for n in range(0, 10):
            if str(n) in self.password:
                return True
        raise ValidationError("Password must have at least one digit")


# I check that password is more (or equal) than 10 words.
class LengthPassword(ABC):
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        if len(self.password) >= 10:
            return True
        raise ValidationError("Password is too short")


# I check that password has at least one upper letter.
class UpperLetterInPassword(ABC):
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        if any([upper_letter.isupper() for upper_letter in self.password]):
            return True
        raise ValidationError("Password must have at least one upper letter")


# I check that password has at least one lower letter.
class LowerLetterInPassword(ABC):
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        if any([lower_letter.islower() for lower_letter in self.password]):
            return True
        raise ValidationError("Password must have at least one lower letter")


# I check that password has at least one special character.
class SpecialCharacterInPassword(ABC):
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        if any(
            [not special_character.isalnum() for special_character in self.password]
        ):
            return True
        raise ValidationError("Password must have at least one special character")


# I check that login is not similar to password.
class LoginSimilarToPassword(ABC):
    def __init__(self, password, login):
        self.password = password
        self.login = login

    def is_valid(self):
        similiary_ratio = fuzz.token_set_ratio(
            self.password.lower().strip(), self.login.lower().strip()
        )
        if similiary_ratio >= 85:
            raise ValidationError("Password is too similar to the login")
        return True


# I chose to use a "try and except" construct. If password is correct -  return True, if not - raise Error.
# If password is correct, the password is hashed.
class LoginAndPasswordValidation:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def is_valid(self):
        validators = [
            DigitsInPassword(self.password),
            LengthPassword(self.password),
            UpperLetterInPassword(self.password),
            LowerLetterInPassword(self.password),
            SpecialCharacterInPassword(self.password),
            LoginSimilarToPassword(self.password, self.login),
        ]
        for validator in validators:
            try:
                validator.is_valid()
            except ValidationError as V:
                print(V)
                return False

        return True

    def hash_password(self):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(self.password.encode("utf-8"), salt)
        return hashed_password
