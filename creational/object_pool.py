


class PooledObject(object):
    
    def __init__(self):
        self.data = "INIT"
    
    def cleenup(self):
        self.data = "INIT"
    
    def __str__(self):
        return str(self.data)




class ObjectPool(object):
    """
        ObjectPool are a Singleton class. It is not thread safe!
        Max objects must be set
    """
    class __ObjectPool:
        def __init__(self, max):
            self.max = max
            self.aviable = []
            self.in_use = []
            
        def get_object(self):
            if len(self.aviable) > 0:
                temp = self.aviable.pop()
                self.in_use.append(temp)
                return temp
            elif ( len(self.aviable) + len(self.in_use)) < self.max:
                temp = PooledObject()
                self.in_use.append(temp)
                return temp
            return None
        
        def return_object(self, obj):
            obj.cleenup()
            self.in_use.remove(obj)
            self.aviable.append(obj)
            
    
    instance = None
            
    def __init__(self, max = 10):
        if not ObjectPool.instance:
            ObjectPool.instance = ObjectPool.__ObjectPool(max)
            
    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    
    
    
pool1 = ObjectPool(2)
obj1 = pool1.get_object()
obj2 = pool1.get_object()

print (obj1)
print (obj2)
obj1.data = 10
obj2.data = 15
print (obj1)
print (obj2)
print ("_______________")

pool2 = ObjectPool(10)  #Max cant be set like this after first init
obj3 = pool2.get_object()
print (obj3," - Is None because no free objects and max objects are created")

pool1.return_object(obj1)
pool2.return_object(obj2)

obj3 = pool2.get_object()
print (obj3)
obj3.data = "Test"
print (obj3)
print ("_______________")

print ("Pool 1 max",pool1.max)
print ("Pool 2 max",pool2.max)
print ("They are the same, they are the same pool. Singleton class")

print ("Avilable objects:",len(pool1.aviable))
print ("Objects in use:",len(pool2.in_use))
        
    
        