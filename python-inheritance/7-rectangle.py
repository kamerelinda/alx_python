"""This module improves the class by raising an exception"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        """instantiation with width and height"""
        super().integer_validator('width', width)
        super().integer_validator('height', height)

    def area(self):
        """calculate and return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """method returns a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
