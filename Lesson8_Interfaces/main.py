#Today's topic is generators
from Lesson8_Interfaces.FileCache import FileCache
from Lesson8_Interfaces.FileReader import FileReader
from Lesson8_Interfaces.Student import Student

#Thos reads a whole file at once. will lag AF if the file is big
# def read_data(path):
#     with open(path) as fp:
#         return [line.strip() for line in fp if line and line[0] != "#"]
#
# for index, line in enumerate(read_data("data.txt")):
#     print("{} {}".format(index+1, line))

#optimize if file is huge and would take a lot of processing power - not the best way, tho
#Reading only a single line
def read_line(fp):
    while True:
        line = fp.readline()
        if line == "":
            return None
        if line and line[0] == "#":
            continue
        return line

# #the yield keyword is used to take value from the function, like "return", but without breaking the function
def generator_1():
    yield 1

def generator_2():
    print("Line 1")
    yield 1
    print("Line 2")
    yield 2
    print("Line 3")
    yield 3
    print("end")

#the best version of reading out files with comments
def read_data(path):
     with open(path) as fp:
         for line in fp:
             line = line.strip()
             if not line:
                 continue
             if line.startswith("#"):
                 continue
             yield line

if __name__ == "__main__":
    fp = open("data.txt")
    print(read_line(fp))

    for num in generator_1():
        print(num)

    for num in generator_2():
        print(num)

    print()

    for index, line in enumerate(read_data("data.txt")):
        print("{} {}".format(index+1, line))

#--- How classes can use interfaces ---

    s1 = Student("John", "Doe", 5)
    s2 = Student("Jan", "Kowalski")

#We can get the student info manually like this"
    print("{} {} {} {}".format(s1.firstname, s1.lastname, s1.year, s1.group))
    print("{} {}".format(s2.firstname, s2.lastname))

# calling an object info looks always the same, so we can make a function about it inside a class
    print(s1.get_name())
#
    print(s1) #shows you a place in memory instead of sth usable. Build a __str__ function in the class file,
    # just to get a get usable stuff

    print(int(s1)) #to view an object s integer we have to build a __int__ class
    print(float(s1)) #to view an object qs float we have to build a __float__ class

#to get a true/false results, we have to put a __bool__ method inside a class
    if s1:
        print("{} is no longer in the first class".format(s1))

    print()

#elementor square braces [], to act as cache

    fileCache = FileCache("data.txt")
    fileCache.readchar(0)
    print(fileCache.cache)
    fileCache.readchar(2)
    print(fileCache.cache)
    fileCache.readchar(1)
    print(fileCache.cache)
    fileCache.readchar(0)
    print(fileCache.cache)

    for line in FileReader("data.txt"):
        print(line)