file_writer = open("text2.txt", "w") #keyword w is overwriting the file
file_writer.write("My content")
file_writer.close()

file_writer = open("text2.txt", "a") #keyword a is appending to the file
file_writer.write(" Line 2")
file_writer.write("\nLine 3")
file_writer.close()

my_list = ["Line 1\n","Line 2\n","Line 3\n",]

file_writer = open("text3_list.txt", "w")
file_writer.writelines(my_list) #writelines is command for lists. Just "write" is for strings
file_writer.close()

#EXERCISES
counter = 0
with open("text3_list.txt") as file_reader:
    for line in file_reader:
        print("Line{}: {}". format(counter, line[:-1]))
        counter += 1

my_list = ["Line 1","Line 2","Line 3"]

file_writer = open("text4.txt", "w")
# file_writer.writelines(my_list) #writelines is command for lists. Just "write" is for strings
file_writer.write("\n".join(my_list) + "\n")
file_writer.close()

print()

#Exercise with names
james_counter = 0
file_reader = open("names.txt")
for line in file_reader:
    print(line[:-1])
    if line.__contains__("James"):
        james_counter += 1
file_reader.close()
print("Found {} James".format(james_counter))