"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """function returns true if the object is an instance of,or if
    object is an instance of a class that inherited from"""
    return isinstance(obj, a_class)
