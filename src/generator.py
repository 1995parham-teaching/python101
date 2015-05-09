# In The Name Of God
# ========================================
# [] File Name : generator
#
# [] Creation Date : 09-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

gen = (value for value in range(10) if value > 5)
lst = [value for value in range(10) if value % 2 == 0]
print(gen)
print(lst)
print(min(lst))
print(min(lst))
print(min(gen))
# we will got error on this :-)
print(min(gen))
