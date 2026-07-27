def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if isinstance(s, str):
        s_list = [ch for ch in s]
        s_list = s_list[::-1]
        new_str = "".join(s_list)
        return new_str
    else:
        print("Input must be a string")

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

string_reverse("Hello World")
string_reverse("Python")