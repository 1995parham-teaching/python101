# In The Name Of God
# ========================================
# [] File Name : descriptors.py
#
# [] Creation Date : 23-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import datetime


class CurrentTime:
    def __get__(self, instance, owner):
        print(self)
        print(instance)
        print(owner)
        return datetime.datetime.now()


class Example:
    time = CurrentTime()


print(Example().time)
