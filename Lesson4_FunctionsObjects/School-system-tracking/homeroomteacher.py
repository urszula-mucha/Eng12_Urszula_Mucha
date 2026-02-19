from person import Person

class HomeroomTeacher(Person):
    def __init__(self, fullname, class_name):
        print("Created entry for a homeroom teacher")
        super().__init__(fullname)
        self.class_name = class_name