# Part A: Predict first. Which exception does each line raise? Then predict the output of the function.

# int("12") value error correct => no exception, returns 12
# int("1.5") type error correct => ValueError (right type, invalid value)
# [1, 2][5]  outOfRange error correct => IndexError
# {}["a"]   indexError correct => KeyError
# "a" + 1 -> type error
# 10 / 0   -> zeroDivisionError

def check(x):
    try:
        result = 10 / x
    except ZeroDivisionError:
        print("B")
        return -1
    else:
        print("C")
        return result
    finally:
        print("D")

print(check(2)) 
print(check(0))

# ouput for check functions
# C
# D
# 5.0
# B
# D
# -1

# but i want to understand why the else excuted when no exception is raised.