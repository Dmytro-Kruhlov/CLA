from Infinity.exceptions import BirthdayException
from datetime import datetime, date
from Infinity.user_interface import IField


class Birthday(IField):
    def __init__(self, value):
        super().__init__()
        self.value = value

    @IField.value.setter
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
