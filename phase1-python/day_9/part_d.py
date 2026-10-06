# Part D: Safe file reader. Write read_file(path) that returns the file's text, or returns None and prints "File not found
# : <path>" if it doesn't exist. 
# Test it with a file that exists (create one first) and one that doesn't.
#  Use a with statement inside the try.
def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

print(read_file("test.txt"))
print(read_file("test1.txt"))