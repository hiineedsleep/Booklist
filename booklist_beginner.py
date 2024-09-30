class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def book_info(self):
        return f"This book's title is {self.title}, author is {self.author}, pages is {self.pages}"

    def long_read(self):
        return self.pages > 300

class Reading_List:
    def __init__(self):
        self.book_list = []

    def add_book(self, read_list):
        self.book_list.extend(read_list)

    def display_books(self):
        for book in self.book_list:
            print(book.book_info())

    def display_long_read(self):
        for book in self.book_list:
            if book.long_read(): # Call the method with parentheses to evaluate it
                print(f"{book.title} has more than 300 pages.")

read_list = Reading_List()
read_list.add_book([Book(title= "To Kill a Mocking Bird", author="Harper Lee", pages=309),
                    Book(title= "The Picture of Dorian Gray", author="Oscar Wilde", pages=256),
                    Book(title= "No Longer Human", author="Osamu Dazai", pages=177),
                    Book(title= "Tender is The Flesh", author="Augustina Bazterica", pages=224)])

read_list.display_books()


read_list.display_long_read()