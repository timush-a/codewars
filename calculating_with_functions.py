number_0 = None
number_1 = None

def seven(function=None):
    """
        If function does not receive arguments,
        then this is the right argument of expression and return number.
        If function gets arguments then, it is the left argument and call math function
        with two global arguments.
    """
    if not function:
       return 7
    else:
        
        global number_0
        number_0 = 7
        print(function.__call__(number_0, number_1))
        
        
def five(function=None):
    global number_1
    if not function:
        number_1 = 5
    else:
        global number_0
        number_0 = 5
        print(function.__call__(number_0, number_1))


def plus(number=None, number_1=None):
    if number_1:
        return number_0 + number_1
    else:
        return plus.__call__
    

seven(plus(five()))
    
    
