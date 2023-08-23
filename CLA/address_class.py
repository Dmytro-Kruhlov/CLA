from CLA.user_interface import IField


class Address(IField):
    def __init__(self, value):
        self.value = value
        self.__value = None

    @IField.value.setter
    def value(self, value):
        self.__value = value

    def __str__(self) -> str:
        return self.__value

    def __repr__(self) -> str:
        return str(self)
