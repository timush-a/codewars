"""
Complete the solution so that the function
will break up camel casing, using a space between words.
Example
solution("camelCasing")  ==  "camel Casing"
"""


def break_camel_case(string):
    result_string = []
    for sym in string:
        if sym.isupper():
            result_string.append(f' {sym}')
        else:
            result_string.append(sym)

    return "".join(result_string)
