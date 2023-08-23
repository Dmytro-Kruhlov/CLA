from CLA.exceptions import BirthdayException
from datetime import datetime, date
from CLA.user_interface import IField


class Birthday(IField):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        try:
            self.__value = datetime.strptime(value, "%Y/%m/%d")
        except:
            raise BirthdayException

    def __str__(self) -> str:
        if self.__value:
            return self.__value.strftime("%d-%m-%Y")

    def __repr__(self) -> str:
        return str(self)
