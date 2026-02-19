from Lesson9_Inheritance.workshop.Vehicles.Car import Car


class Bus(Car):
    def __init__(self, brand, weight, engine, number_of_doors, number_of_passengers):
        super().__init__(brand, weight, engine, number_of_doors)
        self.number_of_passengers = number_of_passengers

    def drive(self):
        self.engine.start()
        self._speed = 120
        print(f"Bus {self.brand} is driving "
              f"at {self._speed} km/h"
              f"with {self.number_of_passengers}")
