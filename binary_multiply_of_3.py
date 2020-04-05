"""
In this kata, your task is to create a regular expression capable of evaluating binary strings
(strings with only 1s and 0s) and determining whether the given string represents a number divisible by 3.

Note
There's a way to develop an automata (FSM) that evaluates if strings representing numbers in a given base are divisible by a given number.
You might want to check an example of an automata for doing this same particular task here.

If you want to understand better the inner principles behind it,
you might want to study how to get the modulo of an arbitrarily large number taking one digit at a time.
"""


PATTERN = re.compile(r'^(0*(1(01*0)*1)*)*$')
