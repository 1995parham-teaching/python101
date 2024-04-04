# In The Name Of God
# ========================================
# [] File Name : pickling.py
#
# [] Creation Date : 23-06-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import pickle


class IntoBinary:
    '''
    Sample class for pickling and un-pickling it.
    '''
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return "My number is " + str(self.number)


if __name__ == '__main__':
    my_object = IntoBinary(10)
    print(my_object)
    pickled = pickle.dumps(my_object)
    print(pickled)
    my_object = pickle.loads(pickled)
    print(my_object)
