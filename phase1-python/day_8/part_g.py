# Part G (stretch): A logger. Write a function log(message) that appends a line to test_run.log in the same folder as the script, in the format 2026-10-06 14:30:05 | message. Call it three times with different messages, then read the file back and print it.
# (Use datetime, Path(__file__).parent, and strftime("%Y-%m-%d %H:%M:%S").)
import datetime as dt
from pathlib import Path

base = Path(__file__).parent
file_path = base / "test_run.log"

def log(message):
	today_date = dt.datetime.now()
	with open (file_path, "a") as file:
		file.write(today_date.strftime("%Y-%m-%d %H:%M:%S") + f" | {message}\n")

log("This is a log message.")
log("This is another log message.")
log("This is yet another log message.")



with open(file_path, "r") as file:
    for line in file:
        print(line.strip())