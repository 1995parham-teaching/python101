# In The Name Of God
# ========================================
# [] File Name : types.py
#
# [] Creation Date : 09-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

number = 10
print("number: %d" % number)
number = 10.1
print("number: %g" % number)
number = 1j
print("number * number: %d" % (number * number).real)
number = 10 / 3
print("10 / 3 = %g" % number)
number = 10 // 3
print("10 // 3 = %d" % number)

print("=========================")

string_one = 'parham\n'
string_two = "parham\n"
print(string_one)
print(string_two)

print("=========================")

my_set = {1, 2, 3, "parham"}
my_list = [1, 2, 3, 'parham']
my_tuple = (1, 2, 10, "python")

print(my_set)
print(my_list)
print(my_tuple)

my_set.add(10)
print(my_set)

print(my_list[0])
print(my_list[-1])
