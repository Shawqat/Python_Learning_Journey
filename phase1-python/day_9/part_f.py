
# Part F: Raise your own. Write validate_age(age): it should raise TypeError("Age must be a number")
#  if age isn't an int, ValueError("Age must be between 0 and 120")
#  if it's out of range, and otherwise return the age. 
# Then write a small tester that calls it with 25, -3, 150, 
# and "ten", catching each exception and printing "OK: 25" or "Rejected: <message>".

def validate_age(age):
    if isinstance(age, int):
        if 0 <= age <= 120:
            return age
        else:
            raise ValueError("Age must be between 0 and 120")
    else:
        raise TypeError("Age must be a number")
        
        
for value in [25, -3, 150, "ten"]:
    try:
        print(f"OK: {validate_age(value)}")
    except (TypeError, ValueError) as e:
        print(f"Rejected: {e}")