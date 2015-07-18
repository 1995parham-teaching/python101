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

    def get_name(self):
        return self.lastName + " " + self.firstName

    @staticmethod
    def static_method():
        return "Hello"

    def unbound_method():
        return "Bye"


contact = Contact("Parham", "Alvani", "Nothing")
print(contact.firstName, contact.lastName)
print(contact.get_name())
print(contact.job)
print("==================")
print(Contact.__dict__)
print(contact.__dict__)
print("==================")
print("==================")
print(contact.static_method())
print(Contact.unbound_method())
print("==================")


class Student(Contact):
    def __init__(self, lname, fname):
        super(Student, self).__init__(lname, fname, 'Student')

    def get_name(self):
        return "New get_name() method"


student = Student("Alvani", "Parham")
print(student.get_name())


class Worker(Contact):
    def __init__(self, lname, fname):
        Contact.__init__(self, lname, fname, 'Worker')
