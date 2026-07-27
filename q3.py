def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct:
        print("Original value of", key, ":", dct[key])
        dct[key] = value
        new_dct = dct
    else:
        dct.update({key:value})
        new_dct = dct

    return new_dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
dct1 = {}
key1 = "name"
value1 = "Alice"
dct1 = update_dictionary(dct1, key1, value1)
# - {"age": 25}, "age", 26
dct2 = {"age": 25}
key2 = "age"
value2 = 26
dct2 = update_dictionary(dct2, key2, value2)