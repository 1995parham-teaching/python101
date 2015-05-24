# In The Name Of God
# ========================================
# [] File Name : introspection.py
#
# [] Creation Date : 10-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import inspect


def example():
    """
    nothing example function.
    :return:
    """
    pass


print(example.__name__)
print(example.__doc__)
print(inspect.getdoc(example))

print((lambda: None).__name__)
