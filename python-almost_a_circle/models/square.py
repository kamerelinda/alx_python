from models.rectangle import Rectangle
"""This module imports methods and arguments from rectangle"""


class Square(Rectangle):
    """This class forms a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiate"""
        super().__init__(size, size, x, y, id)
        """calling the super method in order"""

    def __str__(self):
        """returns a string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter function of retrieving size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method"""
        self.width = value
        self.height = value
