#!/usr/bin/python3

from models.rectangle import Rectangle
"""A square class that inherits from the rectangle class
"""

class Square(Rectangle):
    """A square class

    Args:
        Rectangle (_class_): _a class that takes in in width and height arguments and works with it_
    """
    def __init__(self,size,  x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    @property    
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        """Stores in the size of the circle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >0")
        self.width = value
        self.height = value

        
        
    def __str__(self):
        """Generates the string format of the square class"""
        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - {self.size}"
    
    def update(self, *args, **kwargs):
        """assigns key/value argument to attributes
        """
        
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
        
    def to_dictionary(self):
        """
            Returns the dictionary representation of a Square
        """
        return {'id': getattr(self, "id"),
                'x': getattr(self, "x"),
                'size': getattr(self, "width"),
                'y': getattr(self, "y")}
