# Write a Python program with a function that converts a string to an integer. Handle exceptions within the function and print appropriate error messages.

def string_to_integer(s):
    try:
        result = int(s)
        return result
    except ValueError:
        print("Error: Cannot convert the string to an integer.")
        return None


string = "8945"
integer = string_to_integer(string)
if integer is not None:
    print("Integer value:", integer)
