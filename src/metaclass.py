# In The Name Of God
# ========================================
# [] File Name : metaclass.py
#
# [] Creation Date : 21-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'


class SimpleMetaClass(type):
    def __init__(cls, name, bases, attrs):
        print(name)
        print(cls)
        super(SimpleMetaClass, cls).__init__(name, bases, attrs)


class Example(metaclass=SimpleMetaClass):
    pass

class SubExample(Example):
    pass
