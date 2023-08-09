"""This module creates a rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiate values"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter to retrieve private width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter to set the value of width"""
        self.validation('width', value)
        self.__width = value

    @property
    def height(self):
        """getter to retrieve private height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to set the value of height"""
        self.validation('height', value)
        self.__height = value

    @property
    def x(self):
        """getter to retrieve private x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter to set the value of x"""
        self.validation('x', value)
        self.__x = value

    @property
    def y(self):
        """getter to retrieve private y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter to set the value of y"""
        self.validation('y', value)
        self.__y = value

    @staticmethod
    def validation(name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and name != 'x' and name != 'y':
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and (name == 'x' or name == 'y'):
            raise ValueError("{} must be >= 0".format(name))
