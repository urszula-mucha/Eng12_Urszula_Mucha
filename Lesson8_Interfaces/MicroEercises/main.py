def gen():
    yield 1
    yield 2
    yield "String works as well"

for x in gen():
    print(x)

print()
###############

def reading_file(path):
    with open(path) as f:
        for line in f:
            yield line.rstrip() #rstrip removes linebreaks! https://www.w3schools.com/python/ref_string_rstrip.asp

for line in reading_file("test.txt"):
    print(line)

print()
###################

class Dog:
    def __init__(self, name,):
        self.name = name

#add this bad boi below to show a human text instead of <__main__.Dog object at 0x0000026936C531A0>
    def __str__(self):
        return self.name

d = Dog("Sławek")
print(d)

print()
#####################

class Box:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

b = Box()
b["a"] = 10
print(b["a"])