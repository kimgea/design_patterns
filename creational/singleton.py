
class Singleton:
    class __Singleton:
        def __init__(self, arg):
            self.val = arg
    instance = None
    def __init__(self, arg):
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton(arg)
        else:
            Singleton.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)
    

x = Singleton('sausage')
print(x.val)
y = Singleton('eggs')
print(y.val)
z = Singleton('spam')
print(z.val)
print(x.val)
print(y.val)