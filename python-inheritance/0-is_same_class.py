""" module checks if object is instance of specified class and returns true or false"""


def is_same_class(obj, a_class):
    """Function checks if obj is of instance a_class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
