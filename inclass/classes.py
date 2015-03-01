import time
'''
# WE MAKING SOME CLASS STUFF
class Basic:
    def __init__(self):
        self.var1
        self.var2
        self.var3 = True

    def func1(self, var):
        self.var1
        var

copy.copy( class ) is to make a shallow copy
copy.deepcopy ( class ) is to make a really deep copy
'''

class Rectangle:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.center = [False]*2
    def __str__(self):
        return "I am a rectangle!"
    def __add__(self, number):
        return "I am a rect%dngle! " % number
    def __radd__(self, number):
        return self + number
    def __sub__(self,number):
        return "I am a rect%dngle! " % number
    def __rsub__(self,number):
        return self - number

def find_center(rect):
    for i in xrange(2):
        rect.center[i] = (rect.p1[i] - rect.p2[i])/2.0
    return rect.center

rect = Rectangle([30,422],[5,3])
print find_center(rect)
print rect + 1
print rect - 4
print 1 + rect
print 4 - rect
