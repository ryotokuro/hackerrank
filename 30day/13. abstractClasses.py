from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self): pass


class MyBook(Book):
    def __init__(self, my_title, my_author, my_price):
        super(MyBook,self).__init__(title, author)
        self.title = my_title
        self.author = my_author
        self.price = my_price

    def display(self):
        print("Title:", title)
        print("Author:", author)
        print("Price:", price)


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()