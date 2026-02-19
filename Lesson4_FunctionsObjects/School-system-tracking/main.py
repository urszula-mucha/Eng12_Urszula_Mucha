from teacher import Teacher
from student import Student
from homeroomteacher import HomeroomTeacher


#    --- PREDEFINED UNCHANGABLE ---
#Possible commands of operation
main_commands = [
    "Create",
    "Manage",
    "End"
]

create_commands = [
    "Student",
    "Teacher",
    "Homeroom teacher",
    "End"
]

management_commands = [
    "Class",
    "Student",
    "Teacher",
    "Homeroom teacher",
    "End"
]

#    --- TRACKING ---

teachers = []
homeroom_teachers = []
students = []

#        --- FUNCTIONS ---

#GETTING THE USER CHOICE
#To save the user time and minimize letter mistakes I decided for a number input
def select_from_list(options, name):
    print(f"\nSelect {name}")
    for i, option in enumerate(options, start=1):
        print(f"{i}) {option}")

    while True:
        user_entry = input("Option: ")

        try:
            choice = int(user_entry) - 1

        except ValueError:
            print(f"Please write a number of the chosen {name}.")
            continue

        if 0 <= choice < len(options):
            print(f"You've chosen {name}:", options[choice])
            return options[choice]
        else:
            print("Please select a valid number")

# CREATING A NEW STUDENT OPERATION
def create_student(students):
    print("\nFill the data to add a new student")
    fullname = input("Full name: ")
    class_in = input("Class: ")

    student = Student(fullname, class_in)
    students.append(student)

# CREATING A NEW TEACHER OPERATION
def create_teacher(teacher_list):
    print("\nList of teachers already in the database:")
    for i, t in enumerate(teacher_list, start=1):
        print(f"{i}) {t.fullname}")

    print("\nFill the data to add a new teacher")
    fullname = input("Full name: ")
    subject = input("Subject: ")

    classes = []
    while True:
        class_name = input("Classes taught (leave empty to end the operation): ").strip() #strip to remove eventual empty spaces around the entry

        if not class_name:
            break
        if not (class_name[0].isdigit() and class_name[1].isalpha() and len(class_name) == 2):
            print("Invalid class name. Use format like 3C.")
            continue

        classes.append(class_name)

    teacher = Teacher(fullname, classes, subject)
    teacher_list.append(teacher)

# CREATING A NEW HOMEROOM TEACHER OPERATION
def create_homeroom_teacher(homeroom_teachers_list):
    print("\nList of homeroom teachers already in the database:")
    for i, h in enumerate(homeroom_teachers_list, start=1):
        print(f"{i}) {h.fullname}")

    print("\nFill the data to add a new homeroom teacher")
    fullname = input("Full name: ")

    while True:
        class_name = input("Class name: ").strip() #strip to remove eventual empty spaces around the entry

        if not (class_name[0].isdigit() and class_name[1].isalpha() and len(class_name) == 2):
            print("Invalid class name. Use format like 3C.")
            continue
        break

    homeroom_teacher = HomeroomTeacher(fullname, class_name)
    homeroom_teachers.append(homeroom_teacher)

# MANAGE CLASSES OPERATION
#inspired by Excel join tables logic
def manage_class(students_list, homeroom_teachers_list):
    class_name = input("Class to display: ").strip()

    print("\nStudents:")
    found = False

    for s in students_list:
        if s.class_name == class_name:
            print("-", s.fullname)
            found = True
    if not found:
        print("There are no students in this class")

    for h in homeroom_teachers_list:
        if h.class_name == class_name:
            print("-", h.fullname)
            return

    print("No homeroom teacher found")

# MANAGE STUDENTS OPERATION
def manage_student(students_list, teachers_list):
    fullname = input("Student's full name: ").strip()

    for s in students_list:
        if s.fullname == fullname:
            print(f"\nClass: {s.classes}")
            print("Teachers:")

            found = False
            for t in teachers_list:
                if s.class_name in t.classes:
                    print(f"- {t.subject}: {t.fullname}")
                    found = True

            if not found:
                print("There are no teachers found in this class")
            return

    print("Student not found")

# MANAGE TEACHER OPERATION
def manage_teacher(teachers_list):
    fullname = input("Teacher's full name: ").strip()

    for t in teachers_list:
        if t.fullname == fullname:
            print("\nClasses taught:")
            for c in t.classes:
                print("-", c)
            return
    print("Teacher not found")

# MANAGE HOMEROOM TEACHER OPERATION
def manage_homeroom_teacher(homeroom_teachers_list, students_list):
    fullname = input("Homeroom teacher's full name: ").strip()

    for h in homeroom_teachers_list:
        if h.fullname == fullname:
            print(f"\nClass: {h.class_name}")
            print("Students:")

            for s in students_list:
                if s.class_name == h.class_name:
                    print("-", s.fullname)
            return

    print("Homeroom teacher not found")

# --- ACTUAL PROGRAM ---

while True:
    command_chosen = select_from_list(main_commands, "command")

    if command_chosen == "Create":
        create_choice = select_from_list(create_commands, "command")

        if create_choice == "Teacher":
            create_teacher(teachers)
        elif create_choice == "Student":
            create_student(students)
        elif create_choice == "Homeroom teacher":
            create_homeroom_teacher(homeroom_teachers)
        elif create_choice == "End":
            print("Operations completed")
            break

    elif command_chosen == "Manage":
        manage_choice = select_from_list(management_commands, "command")

        if manage_choice == "Class":
            manage_class(students, homeroom_teachers)
        elif manage_choice == "Student":
            manage_student(students, teachers)
        elif manage_choice == "Teacher":
            manage_teacher(teachers)
        elif manage_choice == "Homeroom teacher":
            manage_homeroom_teacher(homeroom_teachers, students)
        elif manage_choice == "End":
            print("Operations completed")
            break
    elif command_chosen == "End":
        print("Operations completed")
        break