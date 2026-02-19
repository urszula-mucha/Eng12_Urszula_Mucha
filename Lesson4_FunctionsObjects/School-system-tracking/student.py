from person import Person

class Student(Person):
    def __init__(self, fullname, classes):
        print("Created entry for a student")
        super().__init__(fullname)
        self.classes = classes

    def __str__(self):
        return f"{self.fullname}"