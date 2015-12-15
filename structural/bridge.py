"""
    Python version of java example on bridge patterns from
        https://en.wikipedia.org/wiki/Bridge_pattern
"""

#Implementor not needed in python, at least not in this case

 
class DrawingAPI1(object):
    """Concrete Implementor"""
    def draw_circle(self, x, y, radius):
        print('API1.circle at {}:{} radius {}'.format(x, y, radius))



class DrawingAPI2(object):
    """Concrete Implementor"""
    def draw_circle(self, x, y, radius):
        print('API2.circle at {}:{} radius {}'.format(x, y, radius))


#Abstraction not needed in Python, at least not in this case

class CircleShape(object):
    """Refined Abstraction"""
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    # low-level i.e. Implementation specific
    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    # high-level i.e. Abstraction specific
    def resize_by_percentage(self, pct):
        self.radius *= (1 + pct/100.)



#Client
shapes = [
    CircleShape(1, 2, 3, DrawingAPI1()),
    CircleShape(5, 7, 11, DrawingAPI2())
    ]

for shape in shapes:
    shape.resize_by_percentage(2.5)
    shape.draw()