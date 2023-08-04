"""This module improves the class by raising an exception"""


class BaseGeometry:
    """This class defines a base geometry"""
    def area(self):
        """Public instance method that raises an exception method"""
        raise Exception("area() is not implemented")
