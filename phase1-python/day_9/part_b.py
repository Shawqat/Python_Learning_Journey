def safe_int(text):
	try:
		return int(text)
	except ValueError:
		return None
	except TypeError:
		return "Type error"

print(safe_int("42"))
print(safe_int("abc"))
print(safe_int("3.5"))
print(safe_int("7"))
print(safe_int(""))
print(safe_int(None))

# output:
# 42
# None
# None
# 7
# None