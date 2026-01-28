'''
Library management app.
Show all books, add a book, borrow, return, quit the app
'''
from itertools import dropwhile

from Book import Book

def add_book(books, title, author):
    # books.append(Book(title, author))
    new_book = Book(title, author)
    books.append(new_book)
    print(f"added new book: {title} - {author}")

def display_all_book(books):
    if not books:
        print("No books in library")
    else:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book.describe()}")

def save_books_to_file(filename, books): #serialization - convert python object into string
    with open(filename, "w") as file:
        for book in books:
            file.write(book.to_file_format() + "\n")

def from_file_format(line):
    title, author, available = line.strip().split("|")
    return Book(title, author, available == "True")

def read_books_from_file(filename):
    books = []
    with open(filename) as file:
        for line in file:
            books.append(from_file_format(line)) #deserialization - convert string into python object
        return books

if __name__ == "__main__":
    filename = "books.txt"
    books = read_books_from_file(filename)

    while True:
        print("\n--- Menu ---\n")
        print("1. Show all available books")
        print("2. Add a new book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Quit")

        choice = input("Choose the option: ")

        if choice == "1":
            display_all_book(books)
        elif choice == "2":
            title = input("Enter a book title: ")
            author = input("Enter a book author: ")
            add_book(books, title, author)
        elif choice == "3":
            print("Option 3")
        elif choice == "4":
            print("Option 4")
        elif choice == "5":
            print("Opertions completed.")
            save_books_to_file(filename, books)
            break
        else:
            print("Please enter a valid option")
