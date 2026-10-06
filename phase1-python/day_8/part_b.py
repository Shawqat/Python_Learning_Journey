# Part B: Notes app. Write three lines to notes.txt (use "w"),
# then append a fourth, 
# then read the file back and print every line with its 
# number: 1: ..., 2: ....

with open("notes.txt", "w") as f :
	f.write("A\n")
	f.write("B\n")
	f.write("C\n")

with open("notes.txt", "a") as f :
	f.write("D\n")

with open("notes.txt", "r") as f :
	for number , line in enumerate(f, start=1):
		print(f"number: {number}: {line.strip()}")
