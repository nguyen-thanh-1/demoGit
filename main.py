from AddBook import addBook
from ViewBook import viewBook
from DeleteBook import DeleteBook
from BorrowedBook import borrowBook 
from ReturnBook import returnBook

class LibrarySys:
    def __init__(self):
        self.bookList = addBook()
        self.borrowList = borrowBook()
    def displayMenu(self):
        while True:
            print('\n------Library Menu ------')
            print('1. Add Book')
            print('2. View Book')
            print('3. Delete Book')
            print('4. Borrow Book')
            print('5. Return Book')
            print('6. Exit')
            choice = int(input('choose an option: '))
            if choice == 1:
                self.bookList.add()
            elif choice == 2:
                viewBook().view_book(self.bookList)
            elif choice == 3:
                DeleteBook().deleteBook(self.bookList)
            elif choice == 4:
                self.borrowList.borrow(self.bookList)
            elif choice == 5:
                returnBook().return_book(self.bookList, self.borrowList)
            elif choice == 6:
                print('Thank you for using our library system. Goodbye!')
                break
if __name__ == '__main__':
    library = LibrarySys()
    library.displayMenu()