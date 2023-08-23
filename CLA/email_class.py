from CLA.exceptions import EmailException
import re
from CLA.user_interface import IField


class Email(IField):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if re.match(
            r"([A-Za-z]{1}[A-Za-z0-9._]{1,}@[A-Za-z]+\.[A-Za-z]+\.[A-Za-z]{2,})|([A-Za-z]{1}[A-Za-z0-9._]{1,"
            r"}@[A-Za-z]+\.[A-Za-z]{2,})",
            value,
        ):
            self.__value = value
        else:
            raise EmailException

    def __str__(self) -> str:
        return self.__value

    def __repr__(self) -> str:
        return str(self)
