"""This module has an empty class"""


class BaseGeometry:
    """This class passes nothing"""

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
