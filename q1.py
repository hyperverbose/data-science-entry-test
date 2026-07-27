def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if str(x).isnumeric() and str(y).isnumeric():
        x, y = y, x
        return x, y
    else:
        return -1, -1

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
x1 = "Apple"
y1 = 10
x1, y1 = swap(x1,y1)

# - 9, 17
x2 = 9
y2 = 17
x2, y2 =  swap(x2,y2)
