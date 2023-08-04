"""This module has an empty class"""


class BaseGeometry:
    """This class passes nothing"""


def __dir__(cls):
    """Magic method that allows you to override default dir"""
    attributes = super().__dir__()
    """get list of all attributes for this class and exclude __init_subclass"""
    return [attribute for attribute in attributes if attribute != '__init_subclass__']
