# Part C: Validated input. Ask the user for a positive whole number. If they enter text, or zero or negative,
#  say why ("Not a number" vs "Must be positive") and ask again, up to 3 attempts.
#  After 3 failures print "Too many attempts". Print the accepted number otherwise.

def validated_input():
    attempts = 0
    while attempts < 3:
        user_input = input("Please enter a positive whole number: ")
        try:
            number = int(user_input)
            if number <= 0:
                print("Must be positive")
                attempts += 1
            else:
                print(f"Accepted number: {number}")
                return number
        except ValueError:
            print("Not a number")
            attempts += 1
    print("Too many attempts")
    
validated_input()