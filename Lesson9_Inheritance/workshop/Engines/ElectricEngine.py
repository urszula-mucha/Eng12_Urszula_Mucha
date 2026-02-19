from Lesson9_Inheritance.workshop.Engines.Engine import Engine


class ElectricEngine(Engine):
    def __init__(self, power, battery_capacity):
        super().__init__(power)
        self.battery_capacity = battery_capacity

    def start(self):
        print(f"Starting Electric Engine (Max power: {self.power})."
              f"Battery capacity: {self.battery_capacity}")
