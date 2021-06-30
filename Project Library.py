class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print("Books present in this library are:")
        for book in self.books:
            print(book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have issued {bookName}!")
            self.books.remove(bookName)
            
        else:
            print(f"Sorry, {bookName} has already been issued. Please wait till it is returned!")
            

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book!")

class Student:
    def requestBook(self):
        self.book = input("Enter the book you want to borrow:")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book you want to return:")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "PythonNotes"])
    stu = Student()

    while(True):
        welcomeMsg = '''Welcome to Central Library. Please choose an option:
        1. Listing all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the library '''
        print(welcomeMsg)
        
        a = int(input("Enter your choice:"))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(stu.requestBook())
        elif a==3:
            centralLibrary.returnBook(stu.returnBook())
        elif a==4:
            print("Thanks for using this library!")
            exit()
        else:
            print("Invalid choice!")