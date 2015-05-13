# In The Name Of God
# ========================================
# [] File Name : Contact.py
#
# [] Creation Date : 10-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'


class Contact:
    def __init__(self, lname, fname):
        self.lastName = lname
        self.firstName = fname
        self.__private = 1


student = Contact("Alvani", "Parham")
print(student.firstName, student.lastName)
print(student._Contact__private)
