from Lesson9_Inheritance.workshop.Engines.CombustionEngine import CombustionEngine
from Lesson9_Inheritance.workshop.Engines.ElectricEngine import ElectricEngine
from Lesson9_Inheritance.workshop.Vehicles.Car import Car
from Lesson9_Inheritance.workshop.Vehicles.Motorcycle import Motorcycle
from Lesson9_Inheritance.workshop.Vehicles.ElectricCar import ElectricCar

#its an abstract class - we shouldnt make an object from it. here it is just to show a privacy of the speed info
# v1 = Vehicle("Polonez", 1500, "engine 1.4")
#
# print(v1.engine)
# print(v1._speed) #cant access because it's a private class


en1 = ElectricEngine(400, 2000)
en2 = CombustionEngine(200, "petrol")
en3 = ElectricEngine(500, 5000)

tesla = Car("Tesla", 2000, en1, 3)
bike1 = Motorcycle("Yamaha", 300, en2)


future_car = ElectricCar("Vatras", 5000, en3, 5)

vehicles = [tesla, bike1, future_car]

for vehicle in vehicles:
    vehicle.drive()
    vehicle.stop()
    print("***** ***")