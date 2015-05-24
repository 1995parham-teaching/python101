# In The Name Of God
# ========================================
# [] File Name : overloading.py
#
# [] Creation Date : 12-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'


class Hello:
    def __init__(self):
        print("Hello created")

    def __str__(self):
        return "Hello"

    def __int__(self):
        return 110

    def __add__(self, other):
        return other

    def __radd__(self, other):
        return other


h = Hello()
print(str(h))
print(int(h))
print(h + 10)
print(10 + h)
