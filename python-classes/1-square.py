""" This module defines a square"""


class Square:
    """ class that defines a square"""
    def __init__(self, size=0):
        """Instantiate with size equal to 0"""
        self.__size = size
        """private instance attribute"""
        if type(size) != int:
            """if the size is not an integer"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """if size is less than 0"""
            raise ValueError("size must be >= 0")
