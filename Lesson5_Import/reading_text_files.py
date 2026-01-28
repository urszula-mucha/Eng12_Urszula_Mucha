file_reader = open("file.txt")
print(file_reader.read())
file_reader.close() #In python you can read a while file with 3 lines - you have to close the read at the end
print()

file_reader = open("file.txt")
print(file_reader.read(8)) #opens file limited to 8 bits)
file_reader.close()
print()

file_reader = open("file.txt")
print(file_reader.readline()) #reads a single line - returns it as string
print(file_reader.readline())
print(file_reader.readline())
file_reader.close()
print()

file_reader = open("file.txt")
print(file_reader.readline(4)) #reads a single line limited to bits - returns it as string
file_reader.close()
print()

file_reader = open("file.txt")
print(file_reader.readlines()) #reads entire file - gives you list of strings
file_reader.close()
print()

file_reader = open("file.txt")
print(file_reader.readlines(4)) #reads entire file - gives you list of strings based on size in bytes
file_reader.close()
print()

file_reader = open("file.txt")
for line in file_reader:
    print(line)
file_reader.close()

#how to automatically close the file
with open("file.txt") as file_reader:
    for line in file_reader:
        print(line)
print("The file is already closed")