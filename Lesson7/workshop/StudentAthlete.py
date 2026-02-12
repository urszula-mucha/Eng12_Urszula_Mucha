from Lesson7.workshop.Student import Student
from Lesson7.workshop.Athlete import Athlete

#child class/ derived class
class StudentAthlete(Student, Athlete):
    def __init__(self, name):
        super().__init__(name) #executng constructor from parent class

    def introduce(self):
        print(f"I'm {self.name} and I'm a student athlete")