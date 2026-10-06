# Part E: JSON config. Save {"browser": "chromium", "headless": True, "retries": 2} to config.json with indent=2. Load it, change retries to 3, save it again, load it a final time, and print it. 
# Then open config.json in your editor and answer in a comment:
# how does True look in the file?
import json

data = {"browser": "chromium", "headless": True, "retries": 2}

with open("config.json", "w") as f:
	f.write(json.dumps(data, indent=2))
 
with open("config.json", "r") as f:
	loaded = json.loads(f.read())
	loaded["retries"] = 3

with open("config.json", "w") as f:
	f.write(json.dumps(loaded, indent=2))

with open("config.json", "r") as f:
	final_load = json.loads(f.read()) # it converted to true as following json rules
	print(final_load)