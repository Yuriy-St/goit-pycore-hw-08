import re
from constants import PHONE_REGEXP
from field import Field


class Phone(Field):

    def __init__(self, value):
        if self._is_valid_value(value):
            super().__init__(value)
        else:
            raise Exception("The phone number must consist of only 10 digits")

    def _is_valid_value(self, value):
        return re.match(PHONE_REGEXP, value) is not None


if __name__ == "__main__":
    for value in ["123", "abc", "0123456789"]:
        try:
            phone = Phone(value)
            print(f"Phone number: {phone}")
        except Exception as e:
            print(f"Value: {value}, error: {e}")
