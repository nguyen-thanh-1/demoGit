class borrowNode:
    def __init__(self, bid: str, borrower: str):
        self.bid = bid
        self.borrower = borrower
        self.next = None

class borrowBook:
    def __init__(self):
        self.head = None
    
    def borrow(self, bookList):
        bid = input('enter book ID to borrow:')
        borrower = input("enter borrower's name:")
        current = bookList.head
        while current:
            if current.bid == bid and current.status.lower() == "available":
                current.status = "borrowed"
                newBorrow = borrowNode(bid, borrower)
                if self.head is None:
                    self.head = newBorrow
                else:
                    temp = self.head
                    while temp.next:
                        temp = temp.next
                    temp.next = newBorrow
                print(f"book {current.title} is borrowed by {borrower}")
                return
            current = current.next
        print("book not found or not available")
