"""This module improves the class by raising an exception"""


class MetaGeometry:
    """this class overrides the dir init subclass in the class"""

    def __dir__(cls):
        """Magic method that allows you to override default dir"""
        return (attribute for attribute in super().__dir__() if attribute != '__init_subclass__')


class BaseGeometry(MetaGeometry):
    """This class defines a base geometry"""

    def __dir__(cls):
        """Magic method that allows you to override default dir"""
        return (attribute for attribute in super().__dir__() if attribute != '__init_subclass__')

    def area(self):
        """Public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry, MetaGeometry):
    """class that inherits BaseGeometry"""

    def __init__(self, width, height):
        """instantiation with width and height"""
        self.__width = width
        self.__height = height
        """Height and width are private"""
        self.integer_validator('width', self.__width)
        self.integer_validator('height', self.__height)
        """using the integer validator method for our variables"""

    def area(self):
        """calculate and return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """method returns a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __dir__(cls):
        """Magic method that allows you to override default dir"""
        return (attribute for attribute in super().__dir__() if attribute != '__init_subclass__')