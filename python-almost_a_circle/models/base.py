"""This module creates the first class which is a base class"""


class Base:
    """class called Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiate with a blank id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
