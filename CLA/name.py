from CLA.exceptions import Name_Error
from CLA.user_interface import IField


class Name(IField):
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str__(self) -> str:
        return self.__value

    def __repr__(self) -> str:
        return str(self)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) < 3:
            raise Name_Error
        self.__value = value
