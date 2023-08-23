from abc import ABC, abstractmethod
import rich


class IUserOutput(ABC):
    @abstractmethod
    def output(self, value):
        pass


class ConsoleOutput(IUserOutput):

    def output(self, value):
        print(value)


class RichConsoleOutput(IUserOutput):

    def output(self, value):
        rich.print(value)


class IField(ABC):
    @abstractmethod
    def __init__(self):
        self.__value = None

    @property
    @abstractmethod
    def value(self):
        return self.__value

    @value.setter
    @abstractmethod
    def value(self, value):
        self.__value = value
