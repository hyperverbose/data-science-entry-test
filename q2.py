def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    new_lst = [replace_val if val == find_val else val for val in lst]
    return new_lst

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
lst1 = [1, 2, 3, 4, 2, 2]
find_val1 = 2
replace_val1 = 5
mod_lst1 = find_and_replace(lst1, find_val1, replace_val1)

# - ["apple", "banana", "apple"], "apple", "orange"
lst2 = ["apple", "banana", "apple"]
find_val2 = "apple"
replace_val2 = "orange"
mod_lst2 = find_and_replace(lst2, find_val2, replace_val2)