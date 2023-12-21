"""
    This is a documentation of the module part
    it is just a comment
"""

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
         Class constructor.

        If id is not None, assign the public instance attribute id with this argument value.
        Otherwise, increment __nb_objects and assign the new value to the public instance attribute id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects