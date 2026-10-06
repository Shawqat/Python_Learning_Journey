
# Part G: Your first tests with assert. Using your is_even (Day 6) and safe_divide (from the worked example),
#  write at least 6 assertions that check expected results, including edge cases (0, negative numbers, divide by zero). 
# Put them in a function run_tests(). Then deliberately change one assertion so it fails,
#  confirm you get an AssertionError with your message, and change it back.

def is_even(n):
	if n % 2 == 0 :
		return True
	return False

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return "Numbers only"

def run_tests():
    assert is_even(0), "0 should be even"
    assert is_even(-2), "-2 should be even"
    assert not is_even(-3), "-3 should be odd"
    assert safe_divide(10, 2) == 5.0, "10/2 should be 5.0"
    assert safe_divide(10, 0) is None, "divide by zero should give None"
    assert safe_divide(10, "a") == "Numbers only", "string should give 'Numbers only'"
    print("All tests passed")

run_tests()