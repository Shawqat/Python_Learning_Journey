# Part F: Bug hunt. Find and name every problem, including the error type if Python raises one. Then fix them:


# f = open("data.txt", "w")
# f.write("hello")
# content = f.read()
# print(content)

# with open("data.txt", "r") as file
#     for line in file:
#         print(line.strip)

# in first method without using with , we need to close the files with ourself ,
# so it didn't in that snippet so this i think run time error
# also we are trying to read from a file in writing mode
# in second case while using with, we forgot the colon at the end of use so it's syntax error
# also we forgot the parenthesis of strip function so it's wrong output

# so code should be like that 
with open("data.txt", "w") as f:
    f.write("hello")

with open("data.txt", "r") as f:
    content = f.read()
print(content)

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())