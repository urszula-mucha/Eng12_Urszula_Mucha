TPL_FORMAT = "Hello {}" #constans - just a variable but with big letters so we know that it shouldn't be modified

def print_hello(firstname):
    print(TPL_FORMAT.format(firstname))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x * self.y + self.x * self.y) ** 0.5