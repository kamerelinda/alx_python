""" This module defines a square"""


class Square:
    """ class that defines a square"""
    def __init__(self, size=0):
        """Instantiate with size equal to 0"""
        self.__size = size

    @property
    def size(self):
        """getter method to retrieve the private instance size """
        return self.__size

    @size.setter
    def size(self, value):
        """setter method to set the value of a private attribute"""
        self.__size = value
        """private instance attribute"""
        if type(value) != int:
            """if the size is not an integer"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """if size is less than 0"""
            raise ValueError("size must be >= 0")

    def area(self):
        """public instance method called area"""
        return self.__size ** 2
    """returns the square of size"""

    def my_print(self):
        """public method that prints out a square using #"""
        if self.__size > 0:
            """if size is greater than 0"""
            for i in range(self.__size):
                """for the range equal to size"""
                print("#" * self.__size)
                """return # times size"""
        else:
            print(" ")
