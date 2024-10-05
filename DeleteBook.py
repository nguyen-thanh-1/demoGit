class DeleteBook:
    def deleteBook(self, bookList):
        bid = input("enter Book ID to delete:")
        current = bookList.head
        if current.bid == bid:
            bookList.head = current.next
            print("Book deleted successfully")
            return
        while current.next:
            if current.next.bid == bid:
                current.next = current.next.next
                print("Book deleted successfully")
                return
            current = current.next
        print("Book not found")

