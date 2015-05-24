# In The Name Of God
# ========================================
# [] File Name : memoization.py
#
# [] Creation Date : 09-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import functools


def memoize(func):
    """
    Cache the result of the function so it doesn't need to be called
    again, if the same arguments are provided a second time.
    :param func: input function for memoization.
    :return: new function with memoization support.
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        # This line is for demonstration only.
        # Remove it before use it for real.
        print('Calling %s()' % func.__name__)
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


if __name__ == '__main__':
    @memoize
    def multiply(x, y):
        return x * y

    print(multiply(2, 7))
    print(multiply(2, 7))
    print(multiply(2, 2))
