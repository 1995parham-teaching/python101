# In The Name Of God
# ========================================
# [] File Name : inputs.py
#
# [] Creation Date : 14-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

name = input("Please enter your name: ")
print("Hello %s" % name)

number = input("Please enter number: ")
try:
    number = int(number)
except ValueError:
    print("%s is not number" % number)
else:
    print("Your number is %d" % number)