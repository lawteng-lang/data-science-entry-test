def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    return

Comments on Task 1:

This function below checks whether one number can be divided by another number without any remainder.

def check_divisibility(num, divisor):
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return False

    if divisor == 0:
        return False

    return num % divisor == 0


num is the number you want to check
divisor is the number you divide by


How this function works:

It checks if both values are numbers
If one of them is not a number, it returns False
It checks if divisor is 0 because dividing by zero is not allowed
It uses % to find the remainder
If the remainder is 0, it returns True
Otherwise, it returns False


Example:

check_divisibility(10, 2)
10 % 2 is 0
so the function returns: True

------------------------------------------------------------------------------------------------------------------------------

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

Comments on Task 2:

Task 2 need to run the check_divisibility() function with the two number pairs given.

The code is:

check_divisibility(10, 2)
check_divisibility(7, 3)
What happens:

check_divisibility(10, 2)
10 can be divided by 2 with no remainder, so the result is:
True
check_divisibility(7, 3)
7 cannot be divided by 3 evenly because there is a remainder, so the result is:
False

Task 2 is testing for:

1. one example that is divisible
2. one example that is not divisible
