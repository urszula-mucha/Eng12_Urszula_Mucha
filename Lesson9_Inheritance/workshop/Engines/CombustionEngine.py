from Lesson9_Inheritance.workshop.Engines.Engine import Engine


class CombustionEngine(Engine):
    def __init__(self, power, fuel_type):
        super().__init__(power)
        self.fuel_type = fuel_type

    def start(self):
        print(f"Starting combustion engine ({self.fuel_type}),"
              f"power: {self.power} HP")