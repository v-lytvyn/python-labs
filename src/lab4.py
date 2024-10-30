class Book:
    def __init__(self, pages = 100, author = "King", price = 250, year = 2021, publisher = "KSD"):
        self.__pages = pages
        self.__author = author
        self.__price = price
        self.year = year
        self.publisher = publisher

    def get_pages(self):
        return self.__pages

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price   

    def __del__(self):
        print("Object deleted")

    def __str__(self):
        return f"{self.__pages}, {self.__author}, {self.__price}, {self.year}, {self.publisher}"
    
    def __repr__(self):
        return f"Book{self.__pages}, {self.__author}, {self.__price}, {self.year}, {self.publisher}"
   
   
book_1 = Book(300, "George Orwell", 300, 2020, "Secker & Warburg")

book_2 = Book(350, "Jane Austen", 450, 2014, "The Heart's Compass")

book_3 = Book(280, "Virginia Woolf", 200, 2022, "Modernist Books")

book_4 = Book()

print(book_1)

print(book_2)

print(book_3)

print(book_4)




   
# book_1 = Book(760, "King", 250, 2020, "KSD")
# print(book_1)   
   
   
   
#     pages = None
#     author = None
#     price = None

#     def info(self, pages, author, price):
#         print(f"Author: {author}, Pages: {pages}, Price: {price}")


# book_1 = Book()
# book_1.info(760, "King", 550)

