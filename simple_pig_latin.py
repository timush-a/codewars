"""
DESCRIPTION:
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.
Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    pig = []
    for a in text.split():
        if a.isalpha():
            pig.append(a[1:] + a[0] + "ay")
        else:
            pig.append(a)
    return " ".join(pig)
