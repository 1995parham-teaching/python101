# In The Name Of God
# ========================================
# [] File Name : sum.py
#
# [] Creation Date : 14-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'


def sum1(*args):
    answer = 0
    for i in args:
        answer += i
    return answer


def sum2(number_list):
    answer = 0
    for i in number_list:
        answer += i
    return answer


print(sum1(1, 2, 3, 4, 5, 6))
print(sum1())

print(sum2([1, 2, 3]))


def func(**kwargs):
    for i in kwargs:
        print(kwargs[i])


print(func(A=1, B=2, C=3))



















