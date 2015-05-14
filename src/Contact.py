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
    def __init__(self, lname, fname, job):
        self.lastName = lname
        self.firstName = fname
        self.job = job
        self.__private = 1

    def getname(self):
        return self.lastName + " " + self.firstName

    @staticmethod
    def static_method():
        return "Hello"

    def new_method():
        return "bye"


contact = Contact("Parham", "Alvani", "Nothing")
print(contact.firstName, contact.lastName)
print(contact.getname())
print(contact.job)

print("==================")
print(contact.static_method())
print(Contact.new_method())
print("==================")


class Student(Contact):
    def __init__(self, lname, fname):
        super(Student, self).__init__ \
            (lname, fname, 'Student')

    def getname(self):
        return "New getname"


student = Student("Alvani", "Parham")
print(student.getname())


class Worker(Contact):
    def __init__(self, lname, fname):
        Contact.__init__(self, lname, fname, 'Worker')

