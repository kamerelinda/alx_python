"""This module improves the class by raising an exception"""
BaseGeometry = __import__('6-rectangle').Rectangle


class Rectangle(BaseGeometry):
    """class that inherits BaseGeometry"""
    def area(self):
        """calculate and return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """method returns a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
