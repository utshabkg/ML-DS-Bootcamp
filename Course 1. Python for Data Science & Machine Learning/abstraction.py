# Abs class => Abs Method(s) -> Sub Class

from abc import ABC, abstractmethod

class Month(ABC):
    @abstractmethod
    def weeks(self):
        pass

    @abstractmethod
    def days(self):
        pass

class January(Month):
    def weeks(self):
        print("4")
    def days(self):
        print("31")


m = January()
m.days()
m.weeks()