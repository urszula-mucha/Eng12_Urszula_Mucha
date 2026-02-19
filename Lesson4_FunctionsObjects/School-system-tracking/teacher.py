from person import Person

class Teacher(Person):
    def __init__(self, fullname, classes, subject):
        print("Created entry for a teacher")
        super().__init__(fullname)
        self.classes = classes
        self.subject = subject