"""
    Lol, only need to use copy.deepcopy in python
"""
import copy


class A(object):
    def __init__(self,text="test"):
        self.text = text
        
    def __str__(self):
        return self.text
    
    def clone(self):
        return copy.deepcopy(self)
    
    
a = A("test2")


b = copy.deepcopy(a)
c = a.clone()

print (a)
print (b)
print (c)