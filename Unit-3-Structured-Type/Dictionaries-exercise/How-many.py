"""
write a procedure, called how_many, which returns the sum of the number of
values associated with a dictionary. 

e.g.,

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
"""


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here   
    result = 0
    for i in aDict:
        result += len(aDict[i])
    return result


print(how_many(animals))
