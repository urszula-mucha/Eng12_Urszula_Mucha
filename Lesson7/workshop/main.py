from Lesson7.workshop.Student import Student
from Lesson7.workshop.Athlete import Athlete
from Lesson7.workshop.StudentAthlete import StudentAthlete


def introduce_person(person): #polymorphism method
    person.introduce()


student1 = Student("Jack")
athlete1 = Athlete("Will")
student_athlete1 = StudentAthlete("Anna")

student1.introduce()
athlete1.introduce()
student_athlete1.introduce()

print()

introduce_person(student1)
introduce_person(athlete1)
introduce_person(student_athlete1)
