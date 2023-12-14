"""
a function
a sub class
"""

def inherits_from(obj, a_class):
    """ This function is unique to inheriting from a class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class