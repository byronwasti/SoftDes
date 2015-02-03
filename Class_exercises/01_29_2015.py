def is_even(x):
    '''
    Return twice X
    >>> is_even(4)
    True
    >>> is_even(3)
    False
    '''
    return True if x%2 == 0 else False

def string_splosion( string ):
    '''
    Return some weird thing
    >>> string_splosion ( "ab")
    'aab'


    '''
    for i in xrange(len(string)):
        string = string[:i-1] + string
    return string


def gcd(a, b):
    '''
    Return GCD

    >>> gcd(12, 8)
    4
   
    '''
    #print a%b
    return a if b == 0 else gcd(b, a%b)



print gcd(12, 8)

