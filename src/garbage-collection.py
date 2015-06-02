# In The Name Of God
# ========================================
# [] File Name : garbage-collection.py
#
# [] Creation Date : 02-06-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

x = 10
print(id(x))
x = "foo"
print(id(x))
x = None
print(id(x))

a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
del a
print(b)
