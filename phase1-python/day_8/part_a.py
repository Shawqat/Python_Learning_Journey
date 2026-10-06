# Part A: Predict first. Write predictions before running,
#  and flag your least-sure line:

# My prediction : 
# of coures with open and close file automatically, and create a new file if doesn't exist and if it exist clear all data, 
# the file will contain four lines , output like this in file :
# one
# two
# the cursor would be here
with open("a.txt", "w") as f:
    f.write("one\ntwo\n")

# My prediction : 
# it open file and append to last line of the file, 
# also i think of file doesn't exist it would create it and add the first line
# the file will contain five lines , output like this in file :
# one
# two
# 
# three
# the cursor would be here
with open("a.txt", "a") as f:
    f.write("three\n")

# My prediction : 
# it open file and read lines of file with the \n, 
# first print : 3 
# second print : "one\n"
# third print : "one"
with open("a.txt") as f:
    lines = f.readlines()

print(len(lines))
print(lines[0])
print(lines[0].strip())

# My prediction : 
# it open file and clear all it's content because it already exist, write x char
with open("a.txt", "w") as f:
    f.write("x")

# My prediction : 
# output : it would read all lines as one string
with open("a.txt") as f:
    print(f.read())