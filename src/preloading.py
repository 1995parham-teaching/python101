# In The Name Of God
# ========================================
# [] File Name : preloading.py
#
# [] Creation Date : 09-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import functools


def main_function(arg1, arg2, arg3):
    print("arg1 : " + str(arg1))
    print("arg2 : " + str(arg2))
    print("arg3 : " + str(arg3))


partial_function = functools.partial(main_function, arg3=10)
partial_function(20, 30)
