"""This module creates a rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits base"""

    @property
    def width(self):
        """getter to retrieve private width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter to set the value of width"""
        self.__width = value

    @property
    def height(self):
        """getter to retrieve private height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to set the value of height"""
        self.__height = value

    @property
    def x(self):
        """getter to retrieve private x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter to set the value of x"""
        self.__x = value

    @property
    def y(self):
        """getter to retrieve private y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter to set the value of y"""
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiate values"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
