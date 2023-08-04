"""This module  checks if object is an instance
of a class that inherited """


def inherits_from(obj, a_class):
    """function checks if object is an instance of a
    class that inherited from the specified class"""
    return (type(obj) != a_class and issubclass(type(obj), a_class) and
            isinstance(obj, a_class))
