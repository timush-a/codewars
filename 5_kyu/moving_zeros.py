"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)
