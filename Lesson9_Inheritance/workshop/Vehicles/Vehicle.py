from abc import ABC, abstractmethod


#Abc is abstract base class. it prevents from making instances
class Vehicle(ABC):
    def __init__(self, brand, weight, engine):
        self.brand = brand
        self.weight = weight
        self.engine = engine
        self._speed = 0

    @abstractmethod #Mandatory to override in subclasses
    def drive(self):
        pass #pass is "no action". there is no sense to declare "break" or "continue"


    def stop(self):
        self._speed = 0
        print(f"{self.brand} has stopped.")