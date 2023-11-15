import abc
from abc import ABC


class Plate(ABC):

    @abc.abstractmethod
    def description(self):
        pass

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def weight(self):
        pass

    @abc.abstractmethod
    def count(self):
        pass
