def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    return

Comments on Task 1:

This function looks through a list and finds the first negative number.

def find_first_negative(lst):
    i = 0

    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1

    return "No negatives"


i = 0 starts at the first item in the list
while i < len(lst): keeps checking items one by one

if lst[i] < 0: checks if the current item is negative

if it finds a negative number, it returns it immediately
i += 1 moves to the next item

if no negative number is found, it returns "No negatives"

Example:

find_first_negative([3, 5, -2, 7])

How it works :

checks 3 → not negative
checks 5 → not negative
checks -2 → negative
Result: -2

If the list is:

[1, 2, 3]

then the result is: "No negatives"

--------------------------------------------------------------------------



# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]


Comments on Task 2:

Task 2 needs to run the find_first_negative() function with the two lists given.

The code is:

find_first_negative([3, 5, -1, 7, -2, 8])
find_first_negative([2, 10, 7, 0])

How it works:

In [3, 5, -1, 7, -2, 8]
the function checks each number from left to right.
The first negative number it finds is -1.
Result: -1

In [2, 10, 7, 0]
there are no negative numbers in the list.
Result: "No negatives"

Task 2 is testing for:

1.one list that has a negative number
2.one list that has no negative number