left_operand = None
right_operand = None

digits = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def wrapper(digit):
    def generator(function=None):
        """
            If function does not receive arguments,
            then this is the right argument of expression and return number.
            If function gets arguments, then, it is the left argument and call math function
            with two global arguments.
        """
        if not function:
            global right_operand
            right_operand = digit
            return digit
        else:
            global left_operand
            left_operand = digit
            return function.__call__(left_operand, right_operand)
    return generator


zero = wrapper(digits['zero'])
one = wrapper(digits['one'])
two = wrapper(digits['two'])
three = wrapper(digits['three'])
four = wrapper(digits['four'])
five = wrapper(digits['five'])
six = wrapper(digits['six'])
seven = wrapper(digits['seven'])
eight = wrapper(digits['eight'])
nine = wrapper(digits['nine'])


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
