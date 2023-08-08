"""This module has an empty class"""


class MetaGeometry(type):
    """this class overrides the dir init subclass in the class"""

    def __dir__(cls):
        """Magic method that allows you to override default dir"""
        return (attribute for attribute in super().__dir__() if attribute != '__init_subclass__')


class BaseGeometry(metaclass=MetaGeometry):
    """This class passes nothing"""

    def __dir__(cls):
        """Magic method that allows you to override default dir"""
        return [attribute for attribute in super().__dir__() if
                attribute != '__init_subclass__']
