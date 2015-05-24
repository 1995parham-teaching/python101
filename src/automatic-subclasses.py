# In The Name Of God
# ========================================
# [] File Name : automatic-subclasses.py
#
# [] Creation Date : 24-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import random


class Example:
    def __new__(cls, *args, **kwargs):
        cls = random.choice(cls.__subclasses__())
        return super(Example, cls).__new__(cls, *args, **kwargs)


class Spam(Example):
    pass


class Eggs(Example):
    pass


print(Example())
print(Example())
