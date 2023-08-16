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
