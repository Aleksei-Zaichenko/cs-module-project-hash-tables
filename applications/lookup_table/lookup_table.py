# Your code here
import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)  # x ^ y
    v = math.factorial(v)  # v!
    v //= (x + y)  # v // (x + y)
    v %= 982451653

    return v

#Dict will be used as a cache
Dict = {}

def check_for_presence(x, y):

    temp = list(Dict.values())

    for i in range(len(temp)):
        valuesOfXandY = list(temp[i].values())
        if x == valuesOfXandY[0] and y == valuesOfXandY[1]:
            return i
    return False


def get_the_key_from_dictionary(keyIndex):
    temp = list(Dict.keys())
    return temp[keyIndex]


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # check for presence in dictionary

    result = check_for_presence(x, y)
    if result == False: #the dictionary does not have saved (x, y) pair to 'v'
        tempObject = dict({'x': x, 'y': y})

        v = math.pow(x, y)  # x ^ y
        v = math.factorial(v)  # v!
        v //= (x + y)  # v // (x + y)
        v %= 982451653

        #after computation we add the result 'v' to the dictionary
        Dict[v] = tempObject

        return v
    else: #if we can find (x, y) pair in the dictionary, skip all computations and return the result
        return(get_the_key_from_dictionary(result))


for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

