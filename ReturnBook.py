class returnBook:
    def return_book(self, bookList, borrowList):
        if borrowList.head is None:
            print("No borrow list")
            return
        bid = input('enter book ID to return:')
        current = bookList.head
        while current:
            if current.bid == bid:
                current.status = 'available'
                break
            current = current.next

        temp = borrowList.head
        if temp.bid == bid:
            borrowList.head = temp.next
            print('Book returned successfully')
            return
        else:
            while temp.next:
                if temp.next.bid == bid:
                    temp.next = temp.next.next
                    print('Book returned successfully')
                    return
                temp = temp.next
            print('Book not found in borrow list')