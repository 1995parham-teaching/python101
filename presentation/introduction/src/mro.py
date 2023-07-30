class Book:
    def __init__(self, title: str):
        self.title = title
        self.page = 1

    def read(self):
        return f"There sure are a lot of words on page {self.page}"

    def bookmark(self, page):
        self.page = page


class Novel(Book):
    pass


class Mystery(Novel):
    def read(self):
        return f"Page {self.page} and I still don't know how dit it!"


class MysteryBook(Mystery, Book):
    pass


# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases Book, Mystery
# class BookMystery(Book, Mystery):
#    pass


if __name__ == "__main__":
    book = MysteryBook("The Little Prince")
    print(f"New class read(): {book.read()}")
    # L(New) = New + merge(L(Mystery), L(Book))
    # = New + merge(Mystery + L(Novel), L(Book))
    # = New + merge(Mystery + Novel + L(Book), Book)
    # = New + Mystery + Novel + Book
    # New class method resolution order: (
    # <class '__main__.New'>,
    # <class '__main__.Mystery'>,
    # <class '__main__.Novel'>,
    # <class '__main__.Book'>,
    # <class 'object'>,
    # )
    print(f"MysteryBook class method resolution order: {MysteryBook.mro()}")
    # Mystery class method resolution order: (
    # <class '__main__.Mystery'>,
    # <class '__main__.Novel'>,
    # <class '__main__.Book'>,
    # <class 'object'>,
    # )
    print(f"Mystery class method resolution order: {Mystery.mro()}")
