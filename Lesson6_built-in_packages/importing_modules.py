import json
import sys
import os
from os import getcwd
import pickle
import csv
import math
import random
import webbrowser
from datetime import datetime, date
import re

#You have to input them from the terminal
# print(sys.argv[0]) # 0 is reserved for name of the script
# print(sys.argv[1]) # 1 is reserved for parameter1
# print(sys.argv[2]) # 2 is reserved for parameter2

sys.stdout.write("hello world\n") #standard output
sys.stderr.write("Error in color") #error output

print(sys.platform) #recognize operating system
print(sys.maxsize) #returns up to 2^64-1 for 64-bit os, 2^32-1 for 32-bit os

#os.unlink("example.txt") #deleting a file. gives error when file doesn't exist
print(os.getlogin()) #get login user name
print(os.getpid()) # returns id of current process
#print(os.get_terminal_size()) #returns terminal size - need to start the app from the terminal

print(getcwd()) #returns working directory
#os.mkdir("aaaaa")#create a directory from python
#os.remove("aaaaa") #remove the directory/file. same as os.unlink("") command

#os.rename("aaaaa", "bbbbb")  #rename directory/file. its actually a cut-paste command
#print(os.system("systeminfo")) #show info about the system like in terminal
#print(os.system("ipconfig")) #show info about the internet connection

print(os.path.exists("G:\\My Drive\\VaUlat")) #check if a path exists
print(os.path.isdir("G:\\My Drive\\VaUlat")) #check if path leads to a directory or a file
print(os.path.basename("G:\\My Drive\\VaUlat")) #returns parent directory
print(os.path.abspath("..\\lesson6_built_in_packages\\Lesson5_Import\\file.txt")) #change the relative path to absolute. double dot quits the lesson6 folder. Then after slashes we go to the lesson5
print(os.path.abspath("bbbbb")) #easier example. Going just forward to the bbbbb folder.
print(os.path.join("path 1", "path 2")) #joining the given paths

#mac and linux have slashes in other direction than windows.
#absolute path contains root (c:\users...)
#relative path starts where you are

#CONVERTING OBJECT INTO STRING
person = {"name": "Urszula",
          "age": 30,
          "is_programmer": True,
          "skills": ["HTML", "CSS", "Python, SQL"]
          }

json_string = (json.dumps(person)) #changes an object to json string
print(json_string)

#json cant handle set, tuple and None
fd = open("file.json", "w") #SERIALIZATION
fd.write(json_string)
fd.close()

print(json.loads(json_string)) #changes an json string to object - DEserialization

#==================PICKLE======
#serialize tuples, Nones and everything in general rarely used
pickle_string = pickle.dumps(person) #encodes things in binary - you cant really read it until deserialized
print(pickle_string)
fd = open("pickle.pickle", "wb") #write binary and then you should use "rb"
fd.write(pickle_string)
fd.close()

print(pickle.loads(pickle_string))

#============CSV format========
#creating and reading
with open("csv_file.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([1, 2, 3])
    writer.writerow(["a", "b", 4, "example"])

with open("csv_file.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)


#math library
print(math.floor(99.9)) #round the number down
print(math.ceil(99.00001))  #round the number up
print(math.fabs(-10)) #shows an absolut value - removes the minus
print(math.log(5))
print(math.sin(45))
print(math.cos(45))
print(math.fsum([2,3,8]))

#random library
print(random.random()) #returns a random number from 0-1
print(random.randrange(0,10, step=1)) #random in range
print(random.choice(["a", "b", "c"]))

lst = ["opt1", "opt2", "opt3"]
random.shuffle(lst) #mix the list of items
print(lst)

print(random.sample(lst, k=2)) #returns a random sample from a list. In this example choose 2 items (k)

#web browser
#webbrowser.open("https://google.com") #open a web page

#date time
date_now = datetime.now()
print(date_now)
print(date_now.year)

custom_date = date(2025, 1, 24)
print(custom_date)

#========= regex ============
#website version regex101.com - tells you what signs you have.
#used for validation for example if phone number is correctly written

text = "12345"
match = re.match("^\d\d\d\d$", text)

if match:
    print("match")
else:
    print("not match")
