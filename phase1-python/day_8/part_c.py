# Part C: Text analyzer. Create a file story.txt containing at least four lines of any text (you can write it with code). Then read it and print: the number of lines, the total number of words, and the longest word. 
# (Hint: reuse split(), len, and max(words, key=len).)

total_words = 0
all_words = []
with open("story.txt", "w", encoding="utf-8") as f :
	f.write("Welcome to my journey while learning python\n")
	f.write("I feel I'm doing good till now\n")
	f.write("learning python it's a really joy\n")
	f.write("being able to program it's cool")

with open("story.txt", "r", encoding="utf-8") as f :
	lines = f.readlines()
	for line in lines:
		line = line.strip()
		print(line)
		line_list = line.split()
		total_words += len(line_list)
		all_words.extend(line_list)

print(f"number of lines: {len(lines)}, longest word: {max(all_words, key=len)}")