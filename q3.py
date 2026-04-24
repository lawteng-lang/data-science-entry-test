def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    return

Comments on Task 1: 

This function adds or updates a key and value in a dictionary.

def update_dictionary(dct, key, value):
    if key in dct:
        print(dct[key])

    dct[key] = value
    return dct


dct is the dictionary
key is the name you want to add or update
value is the new value for that key

How it works:

It checks if the key is already in the dictionary
If the key already exists, it prints the old value
Then it puts the new value into the dictionary
Finally, it returns the updated dictionary

Example:

update_dictionary({"name": "John"}, "name", "Mike")
What happens:

"name" already exists
it prints: "John"
then it changes "name" to "Mike"
Result:

{"name": "Mike"}
If the key does not exist, it just adds it.

--------------------------------------------------------------------------

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

Comments on Task 2:

This task needs to use the update_dictionary() function with the two examples given.

The code is:

update_dictionary({}, "name", "Alice")
update_dictionary({"age": 25}, "age", 26)
Simple meaning:

1st example:

update_dictionary({}, "name", "Alice")

Note: The dictionary is empty, so "name" is added with value "Alice".
Result:

{"name": "Alice"}

2nd Example:

update_dictionary({"age": 25}, "age", 26)

Note: The key "age" already exists, so the function first prints the old value:
25 Then it updates "age" to 26.

Result:

{"age": 26}

So Task 2 is just merely testing the function with:

1. one new key
2. one existing key that gets updated


Coding Example:

print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))

