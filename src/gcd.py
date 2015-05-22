# In The Name Of God
# ========================================
# [] File Name : gcd.py
#
# [] Creation Date : 22-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(10, 3))
