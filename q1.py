def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return

Comment on Task 1: 

This function swaps the values of x and y without using a third variable.

If either x or y is not a number, it returns -1.

If both are numbers, it swaps them like this:

x = x + y
y = x - y
x = x - y
Example with x = 5 and y = 10:

x = 5 + 10 becomes 15
y = 15 - 10 becomes 5
x = 15 - 5 becomes 10
Now the values are swapped:
x = 10, y = 5

Then the function prints the swapped values.

Example:

swap(5, 10)   # prints: 10 5
swap("5", 10) # returns: -1

---------------------------------------------------------------------------------

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17


Comments on Task 2:

Task 2 does not need a new function, we need to run the swap() function using the two values given.

The two function calls are:

swap("Apple", 10)
swap(9, 17)

2 scenerios will happen:

swap("Apple", 10)
"Apple" is not a number, so the function returns -1.

swap(9, 17)
Both values are numbers, so the function swaps them and prints:

So in simple words, Task 2 is just testing the swap() function with one invalid input and one valid input.
