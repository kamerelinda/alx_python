"""This module improves the class by raising an exception"""


class Metaclass:
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass']


class BaseGeometry(metaclass=Metaclass):
    """This class defines a base geometry"""
    def __dir__(cls):
        """Magic method that allows you to override default dir"""
        return [attribute for attribute in super().__dir__()
                if attribute != '__init_subclass']

    def area(self):
        """Public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
