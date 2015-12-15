"""
    NEXT
        - Make a singleton like lazy decorator to lazy load 
            property/method single time for all instances of object???
"""

def lazy_property(fn):
    """Decorator that makes a property lazy-evaluated."""
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazy_property

def lazy_method(fn):
    """Decorator that makes a method lazy-evaluated."""
    attr_name = '_lazy_' + fn.__name__

    def _lazy_method(self,*args, **kw):
        if not hasattr(self, attr_name) or kw.get("new_process",False):
            setattr(self, attr_name, fn(self,*args, **kw))
        return getattr(self, attr_name)
    return _lazy_method


class Person(object):
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume that it costs much time.
        print ("long relatives processing")
        relatives = "Many relatives."
        return relatives
    
    @lazy_method
    def friends(self, new_process=False):
        # Get all relatives, let's assume that it costs much time.
        print ("Long friends processing")
        relatives = "Many friends."
        return relatives



jhon = Person('Jhon', 'Coder')
print("Before we access `relatives`:")
print(jhon.__dict__)
print ("__________________")
print ("Access relatives and friends from first time")
print("Jhon's relatives: {0}".format(jhon.relatives))
print("Jhon's relatives: {0}".format(jhon.friends()))
print ("______________________")
print("After we've accessed `relatives and friends`:")
print(jhon.__dict__)
print ("______________")
print ("Get firend and relatives. Not processing from scratch")
print (jhon.relatives)
print (jhon.friends())
print ("___________________")
print ("Process friends from scratch")
print (jhon.friends(new_process=True))

