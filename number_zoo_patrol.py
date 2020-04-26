"""
Task:
Write a function that takes a shuffled list of unique numbers from 1 to n with one element
missing (which can be any number including n). Return this missing number.

Note: huge lists will be tested.

Examples:
[1, 3, 4]  =>  2
[1, 2, 3]  =>  4
[4, 2, 3]  =>  1
"""


def find_missing_number(numbers):
    if numbers:
        result = set.difference(set(range(1, max(numbers) + 1)), set(numbers))
        if result:
            return result.pop()
        else:
            return max(numbers) + 1
    else:
        return 1
