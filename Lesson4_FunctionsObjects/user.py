class User: #class is a template (schema) to create objects (instances of class)
    def __init__(self, name, age): #method CONSTRUCTOR
        print("Creating instance of class user")
        self.name = name
        self.age = age

    def print_hello(self):
        print("Hello " + self.name)
        #print("Hello {}, {}".format(self.name, self.age))

    def print_bye(self):
        print("Bye {}".format(self.name))

