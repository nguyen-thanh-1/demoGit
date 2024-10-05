class viewBook:
    def view_book(self, bookList):
        current = bookList.head
        if current is None:
            print("No books in the library.")
            return
        print(f"{'Bid':<10} {'Title':<20} {'Author':<20} {'Status':<10}")
        while current:
            print(f"{current.bid:<10} {current.title:<20} {current.author:<20} {current.status:<10}")
            current = current.next