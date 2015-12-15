

class A(object):
    def __init__(self,text="test"):
        self.text = text
        
    def __str__(self):
        return self.text


def f1():
    """
        Simple Factory
    """
    return A()


def f2():
    """
        Simple factory implementing the Singleton pattern
    """
    if f2.obj is None:
        f2.obj = A()
    return f2.obj
f2.obj = None



print ("Test simple factory")
a = f1()
print (a)

print ("Test simple factory singleton")
a2 = f2()
a2.text = "text"
print (a2)
a3 = f2()
print (a3)

print ("Test simple factory singleton - change value")
a3.text = "Rock"
print (a2)
print (a3)
