"""
Description:
This time we want to write calculations using functions and get the results.
Requirements:
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following
mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
Let's have a look at some examples:
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
"""


left_operand = None
right_operand = None


def wrapper(digit):
    def number_function_generator(function=None):
        """
            If function does not receive arguments,
            then this is the right argument of expression and return number.
            If function gets arguments, then, it is the left
            argument and call math function with two global arguments,
            which change during function call numbers
        """
        if not function:
            global right_operand
            right_operand = digit
            return digit
        else:
            global left_operand
            left_operand = digit
            return function.__call__(left_operand, right_operand)
    return number_function_generator


zero = wrapper(0)
one = wrapper(1)
two = wrapper(2)
three = wrapper(3)
four = wrapper(4)
five = wrapper(5)
six = wrapper(6)
seven = wrapper(7)
eight = wrapper(8)
nine = wrapper(9)


def plus(left=None, right=None):
    if right is not None:
        return left + right
    else:
        return plus.__call__


def times(left=None, right=None):
    if right is not None:
        return left * right
    else:
        return times.__call__


def minus(left=None, right=None):
    if right is not None:
        return left - right
    else:
        return minus.__call__


def divided_by(left=None, right=None):
    if right is not None:
        return left // right
    else:
        return divided_by.__call__
