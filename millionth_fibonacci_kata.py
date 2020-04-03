"""
In this kata you will have to calculate fib(n) where:
fib(0) := 0
fib(1) := 1
fin(n + 2) := fib(n + 1) + fib(n)
Write an algorithm that can handle n up to 2000000.
Your algorithm must output the exact integer answer, to full precision.
Also, it must correctly handle negative numbers as input.
HINT I: Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n)
to find fib(n) if you already know fib(n + 1) and fib(n + 2)?
Use this to reason what value fib has to have for negative values.
"""

def calc(num):
    if num == 0:
        return (0, 1)
    elif num == 1:
        return (1, 1)
    else:
        a, b = calc(num // 2)
        p = a * (2 * b - a)
        q = b * b + a * a
        return (p, q) if num % 2 == 0 else (q, p + q)


def fib(num):
    if num >= 0:
        return calc(num)[0]
    else:
        return -calc(-num)[0] if num % 2 == 0 else calc(-num)[0]
