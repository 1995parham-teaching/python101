# In The Name Of God
# ========================================
# [] File Name : functions.py
#
# [] Creation Date : 10-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'


def square(x):
    if not isinstance(x, int):
        print("Error: x is a %s instead of int." % type(x))
    else:
        return x * x


def square2(x):
    if not hasattr(x, '__mul__'):
        print("Error: your object do not support multiplication")
    else:
        return x * x


print(square(10))
print(square2(10.1))
