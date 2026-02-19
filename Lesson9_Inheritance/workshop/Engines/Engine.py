from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self, power):
        self.power = power

    @abstractmethod
    def start(self):
        pass
