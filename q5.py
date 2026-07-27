def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if str(num).isnumeric() and str(divisor).isnumeric():
        if num%divisor == 0:
            return True
        else:
            return False
    else:
        print("Inputs must be numeric.")

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
check_divisibility(10, 2)
check_divisibility(7, 3)