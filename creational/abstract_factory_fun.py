
class Rectangle(object):
    def draw(self):
        print ("Rectangle draw() method")
        
class Square(object):
    def draw(self):
        print ("Square draw() method")

class Read(object):
    def fill(self):
        print ("Read fill")

class Blue(object):
    def fill(self):
        print ("Blue fill")
        
        
###############################
# More dynamic and less rigid factories. More responsebilitie on package users

class BaseFactory(object):
    def __init__(self, data={}):
        self.data = data
    def get_data(self,key):
        return self.data.get(key,None)
    def set_data(self,key, value):
        self.data[key] = value
        
class ShapeFactory(BaseFactory):
    def __init__(self,shapes={"rectangle":Rectangle()}):
        super(ShapeFactory,self).__init__(shapes)
        
class ColorFactory(BaseFactory):
    def __init__(self,colors={"read":Rectangle()}):
        super(ColorFactory,self).__init__(colors)
        
#Factory Producer
class FactoryProducer(BaseFactory):
    def __init__(self, factories={"shape":ShapeFactory()}):
        super(FactoryProducer,self).__init__(factories)
        
    def getFactory(self,factory_name):
        return self.data.get(factory_name.lower(),None)
    
producer = FactoryProducer()
producer.set_data("color", ColorFactory())
factory = producer.getFactory("color")
factory.set_data("read",Read())
product = factory.get_data("read")   
product.fill()


##################################
# Shorter but same as original in abstract_factory.py
def sf(shape):
    if shape.lower() == "rectangle": return Rectangle()
    elif shape.lower() == "square": return Square()
    
def cf(color):
    if color.lower() == "blue": return Blue()
    elif color.lower() == "read": return Read()

def fp(factory):
    if factory.lower() == "shape": return sf
    elif factory.lower() == "color": return cf

factory = fp("shape")
product = factory("rectangle")
product.draw()


###########################
#Functions below is dangerous if user can manipulate input string
############################
import sys
product = getattr(sys.modules[__name__], "Blue")()
product.fill()

#############################
product = eval("Blue")()
product.fill()

#####################
product = globals()["Blue"]()
product.fill()
 
