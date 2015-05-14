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


contact = Contact("Parham", "Alvani", "Nothing")
print(contact.firstName, contact.lastName)
print(contact.job)


class Student(Contact):
    def __init__(self, lname, fname):
        super(Student, self).__init__(lname, fname, 'Student')


class Worker(Contact):
    def __init__(self, lname, fname):
        Contact.__init__(self, lname, fname, 'Worker')


student = Student("Alvani", "Parham")
print(student.firstName, student.lastName)
print(student.job)
print(student._Contact__private)

worker = Worker("Alvani", "Parham")
print(worker.firstName, worker.lastName)
print(worker.job)
print(worker._Contact__private)
