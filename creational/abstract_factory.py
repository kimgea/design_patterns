

from abc import ABCMeta, abstractmethod

###########################
#
#    Product
####

#Abstract Product
class AbstractShape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass
    
class AbstractColor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def fill(self):
        pass
    
#Concreat Product
class Rectangle(AbstractShape):
    def draw(self):
        print ("Rectangle draw() method")
        
class Square(AbstractShape):
    def draw(self):
        print ("Square draw() method")

class Read(AbstractColor):
    def fill(self):
        print ("Read fill")

class Blue(AbstractColor):
    def fill(self):
        print ("Blue fill")
    
    
        
###########################
#
#    Factory
####

#Abstract Factory
class AbstractFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getShape(self):
        pass
    
    @abstractmethod
    def getColor(self):
        pass

#Concreat Factory
class ShapeFactory(AbstractFactory):
    def getShape(self, shapetype):
        try:
            if shapetype.lower() == "rectangle":
                return Rectangle()
            elif shapetype.lower() == "square":
                return Square()
        except: pass
        raise TypeError('Unknown Shape.')
    
    def getColor(self, colortype):
        return None

class ColorFactory(object):
    def getShape(self, shapetype):
        return None
    
    def getColor(self, colortype):
        try:
            if colortype.lower() == "read":
                return Rectangle()
            elif colortype.lower() == "blue":
                return Square()
        except: pass    #Bad exception
        raise TypeError('Unknown Color.')
    
#Factory Producer
class FactoryProducer():
    @staticmethod
    def getFactory(factory_name):
        try:
            if factory_name.lower() == "shape":
                return ShapeFactory()
            elif factory_name.lower() == "color":
                return ColorFactory()
        except:pass #Bad exception
        raise TypeError('Unknown Factory.')
    
    

        

        
        
shape_factory = FactoryProducer.getFactory("shape")
circle = shape_factory.getShape("square")
circle.draw()


