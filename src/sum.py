# In The Name Of God
# ========================================
# [] File Name : sum.py
#
# [] Creation Date : 14-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'


def var_sum(*args):
    answer = 0
    for i in args:
        answer += i
    return answer


def list_sum(number_list):
    answer = 0
    for i in number_list:
        answer += i
    return answer


print(var_sum(1, 2, 3, 4, 5, 6))
print(var_sum())

print(list_sum([1, 2, 3]))


def dic_sum(**kwargs):
    answer = 0
    for key, value in kwargs.items():
        print('[' + str(key) + ']' + ' = ' + str(value))
        answer += value
    return answer


print(dic_sum(A=1, B=2, C=3))
