"""
Write a procedure called oddTuples, which takes a tuple as input, and returns a
new tuple as output, where every other element of the input tuple is copied,
starting with the first one.
"""


def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    return aTup[::2]


#print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
# ('I', 'a', 'tuple')
