def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    return

Comments on Task 1:

This Function below checks if lst is actually a list. If not a list, Function will stop and gives back -1 to show invalid input.

 if not isinstance(lst, list):
        return -1

    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst


Coding Example:

find_and_replace("hello", "l", "x")
Here, "hello" is a string, not a list, so the function returns -1. 

--------------------------------------------------------------------------------------------------------------------


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"


Comments on Task 2:

Our Tasks are as follows:

In the first list, find every 2 and change it to 5.
Result:[1, 5, 3, 4, 5, 5]

In the second list, find every "apple" and change it to "orange"
Result: ["orange", "banana", "orange"]

So Task 2 is just testing the function with two different lists to see if it replaces the values correctly.


Coding Example: 

print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))