import types

"""
    Concreet adaptee classes.
    Interface class with get_x1 and getX2 methods not needed in python
"""

class APIa(object):
    def get_x1(self,x,y):
        return x+y
    
class APIb(object):
    def getX2(self,x):
        return x
    
    
    
"""
    Adapter class
"""

class Adapter(object):
    """
        Adapter
    """
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        
        for i in adapted_methods:
            if callable(adapted_methods[i]):
                self.set_adapted_method(i, adapted_methods[i])
            else:
                self.__dict__[i] = adapted_methods[i]
        
    def __getattr__(self, attr):
        return getattr(self.obj, attr)
    
    def set_adapted_method(self, name, method):
        self.__dict__[name] = types.MethodType( method, self )
    

objects = []
apia = APIa()
objects.append(Adapter(apia, get_x=apia.get_x1(1,2)))
apib = APIb()
objects.append(Adapter(apib, get_x=apib.getX2(2)))

print ("Use adapter class to acces other classes with get_x")
for i in objects:
    print (i.get_x)
print ("______________")


def get_x(self,x):
    """
        Custom method to access API1
    """
    return self.obj.get_x1(x,2)


adapter = Adapter(APIa(),test=get_x, get_x=apia.get_x1(1,2))
print ("Access apia with custom adpater method from addapter",adapter.test(5))
print ("Access apia with get_x from adapter",adapter.get_x)

