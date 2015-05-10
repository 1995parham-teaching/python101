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
# print(min(gen))


def fibonacci(count):
    # These seed values generate 0 and 1 when fed into the loop
    a, b = -1, 1
    while count > 0:
        # Yield the value for this iteration
        c = a + b
        yield c
        # Update values for next iteration
        a, b = b, c
        count -= 1


print("Fibonacci sequence: ")
for x in fibonacci(10):
    print(x)