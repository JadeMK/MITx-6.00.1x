"""
write a procedure, called biggest, which returns the key corresponding to the
entry with the largest number of values associated with it. If there is more
than one such entry, return any one of the matching keys.

e.g.,
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
"""


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    largest = 0
    result = ""
    if len(aDict) == 0:
        return
    for i in aDict:
        if len(aDict[i]) >= largest:
            largest = len(aDict[i])
            result = i
    return result


# print(biggest(animals))
