from Infinity.exceptions import Name_Error
from Infinity.user_interface import IField


class Name(IField):
    def __init__(self, value):
        self.value = value
        super().__init__()

    def __str__(self) -> str:
        return self.__value

    def __repr__(self) -> str:
        return str(self)

    @IField.value.setter
    def value(self, value):
        if len(value) < 3:
            raise Name_Error
        self.__value = value
