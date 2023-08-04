"""This module improves the class by raising an exception"""


class BaseGeometry:
    """This class defines a base geometry"""
    def __dir__(cls) -> None:
        """Magic method that allows you to override default dir"""
        attributes = super().__dir__()
        """get list of all attributes for this class and exclude __init_subclass"""
        list_to_return = []
        for attr in attributes:
            if attr != '__init_subclass__':
                """append this to the list_to_return"""
                list_to_return.append(attr)
        return list_to_return

    def area(self):
        """Public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
