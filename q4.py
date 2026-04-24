def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    return

Comments on Task 1:

This function takes a string and returns it in reverse order.

def string_reverse(s):
    if not isinstance(s, str):
        return -1

    return s[::-1]


It first checks if s is a string
If s is not a string, it returns -1
If s is a string, it reverses the letters and returns the new string


Coding Example:

string_reverse("hello")
Result: "olleh"

The part s[::-1] is what reverses the string. It reads the string from the end to the beginning.

-------------------------------------------------------------------------------------------------------


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"


Comments on Task 2:

The code is:

string_reverse("Hello World")
string_reverse("Python")
What happens:

"Hello World" is reversed to:
"dlroW olleH"
"Python" is reversed to:
"nohtyP"

So in simple words, Task 2 is just testing the function with two strings to make sure it reverses them correctly.