from CLA.exceptions import PhoneMustBeNumber
from CLA.sanytize import sanitize_phone_number
from CLA.user_interface import IField


class Phone(IField):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        sanytized_ph = sanitize_phone_number(value)
        if sanytized_ph is None:
            raise PhoneMustBeNumber
        self.__value = sanytized_ph

    def __str__(self) -> str:
        return self.__value

    def __repr__(self) -> str:
        return str(self)
