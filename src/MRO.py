# In The Name Of God
# ========================================
# [] File Name : MRO.py
#
# [] Creation Date : 10-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'


class Book:
    def __init__(self, title):
        self.title = title
        self.page = 1

    def read(self):
        return "There sure are a lot of words on page %d" % self.page

    def bookmark(self, page):
        self.page = page


class Novel(Book):
    pass


class Mystery(Novel):
    def read(self):
        return "Page %d and I still don't know how dit it!" % self.page


class New(Mystery, Book):
    pass


book = New("The Little Prince")
print(New.__mro__)
print(book.read())
