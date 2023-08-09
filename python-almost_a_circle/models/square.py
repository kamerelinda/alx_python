from models.rectangle import Rectangle
"""This module imports methods and arguments from rectangle"""


class Square(Rectangle):
    """This class forms a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
