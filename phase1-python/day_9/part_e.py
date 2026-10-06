# Part E: Bug hunt. Find and name every problem, including each error type (or the lack of one), then fix them:

# def get_item(items, index):
#     try:
#         return items[index]
#     except:
#         print("Something went wrong")

# result = get_item([1, 2, 3], 5)
# print(result + 1)

# try:
#     number = int("abc")
# except ValueError
#     print("Not a number")
# finally:
#     print("Done")

# (Three problems: one is a syntax error, one is a runtime error that happens because of a design problem, and one is a design problem in itself. Say which is which.)
# syntax error : the missing colon of the second except statement
# runtime error : result = get_item([1, 2, 3], 5) in that line cause the 5 index is out of range error
# also i think this design problem print(result + 1) cause these two lines should be inside try out block.
# i think also there should be more exceptions for handling out of range , and the type of list 


def get_item(items, index):
    try:
        return items[index]
    except (IndexError, TypeError) as e:
        print(f"Could not get item: {e}")
        return None

result = get_item([1, 2, 3], 5)
if result is None:
    print("No item found")
else:
    print(result + 1)
    
try:
    number = int("abc")
except ValueError:
    print("Not a number")
finally:
    print("Done")