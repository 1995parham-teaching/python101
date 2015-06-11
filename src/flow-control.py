# In The Name Of God
# ========================================
# [] File Name : flow-control.py
#
# [] Creation Date : 09-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

number = input("please enter number: ")
number = int(number)
if number % 2 == 0:
    print("your number is even")
else:
    print("your number is odd")

# for loop with else statement
for i in range(2, number // 2):
    if number % i == 0:
        break
else:
    print("your number is prime")
