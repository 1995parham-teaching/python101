# In The Name Of God
# ========================================
# [] File Name : count-lines2.py
#
# [] Creation Date : 15-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

filename = input("Please enter your filename: ")
fo = open(filename, "r")
counter = 0
while True:
    line = fo.readline()
    if not line:
        break
    counter += 1
    print(line)
print(counter)
