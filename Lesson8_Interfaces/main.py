#Today's topic is generators
from Lesson8_Interfaces.FileCache import FileCache
from Lesson8_Interfaces.FileReader import FileReader
from Lesson8_Interfaces.Student import Student


def read_data(path):
    with open(path) as fp:
        return [line.strip() for line in fp if line and line[0] != "#"]

for index, line in enumerate(read_data("data.txt")):
    print("{} {}".format(index+1, line))

#optimize if file is huge and would take a lot of processing power - not the best way, tho
# def read_line(fp):
#     while True:
#         line = fp.readline()
#         if line == "":
#             return None
#         if line and line[0] == "#":
#             continue
#         return line

def read_data(path):
     with open(path) as fp:
         for line in fp:
             if line and line[0] != "#":
                 continue
             yield line.strip()

#the yield keyword is used to take value from the function, like "return", but without breaking the function
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

if __name__ == "__main__":
    fp = open("data.txt")
    #print(read_line(fp))

    for num in generator_1():
        print(num)

    print()

    for index, line in enumerate(read_data("data.txt")):
        print("{} {}".format(index+1, line))

    s1 = Student("John", "Doe", 5)
    s2 = Student("Jan", "Kowalski")
    print("{} {} {} {}".format(s1.firstname, s1.lastname, s1.year, s1.group))
    print("{} {}".format(s2.firstname, s2.lastname))

    print(s1.get_name())

    print(s1) #shows you a place in memory instead of sth usable. Put __str__ in the class file, to get usable stuff

    print(int(s1))
    print(float(s1))

    if s1:
        print("{} is no longer in the first class".format(s1))

    print()

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