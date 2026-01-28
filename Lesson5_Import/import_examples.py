# import file_name
# from file_name import class/ variable_name/ function
from Lesson5_Import.helper import TPL_FORMAT, print_hello, Point
from Lesson5_Import.helper2 import TPL_FORMAT #in case of conflict with names, the newer one is used
from Lesson5_Import.helper2 import print_hello as print_formal_hello



print(TPL_FORMAT.format("Urszula"))
print_hello("Kamil")
print_formal_hello("Kamil")

p1 = Point(3, 4)
p2 = Point(5, 12)

print(p1.length() + p2.length())