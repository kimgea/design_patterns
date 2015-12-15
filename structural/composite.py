


#Component not needed in Python


class Composite(object):
    """Composite class"""
    def __init__(self, children=[]):
        self.children = children
        
    def read(self):
        for child in self.children:
            child.read()
    
    def add_child(self, child):
        self.children.append(child)
        
    def remove_child(self, child):
        self.children.remove(child)
        
        

class Leaf(object):
    """Leaf class"""
    def __init__(self, val):
        self.val = val
        
    def read(self):
        print (self.val)
        
        

composite1 = Composite([Leaf("one"), Leaf("two"), Leaf("tre")])
composite2 = Composite([Leaf("four"),])
composite = Composite([composite1,composite2])

composite.read()
        