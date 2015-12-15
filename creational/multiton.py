


class Multiton:
    class __Multiton:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instances = {}
    def __init__(self, key,value):
        self.key = key        
        if key not in Multiton.instances:
            Multiton.instances[key] = Multiton.__Multiton(value)
        else:
            Multiton.instances[key].val = value
    def __getattr__(self, name):
        return getattr(self.instances[self.key], name)


x = Multiton("one","test")
print (x.val)

print ("________________________")
z = Multiton("one","test2")
print (z.val)
print (x.val)


print ("________________________")
y = Multiton("two","test666")
print (z.val)
print (x.val)
print (y.val)


print ("________________________")
w = Multiton("two","Hello")
print (z.val)
print (x.val)
print (w.val)
print (y.val)