"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalize
Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
"""
import re


def to_camel_case(text):
    words = re.findall(r"[a-zA-Z]+", text)
    if not len(words):
        return text
    else:
        camel_case = words[0]
        for word in words[1:]:
            camel_case += (word.lower()).capitalize()

    return camel_case
