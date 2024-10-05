
class node:
    def __init__(self, bid : str, title: str, author: str, status: str):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status
        self.next = None
class addBook:
    def __init__(self):
        self.head = None
       
    def add(self):
        bid = input("enter book ID:")
        title = input("enter book title:")
        author = input("enter book author:")
        status = input("enter book status (0 - available):")
        newBook = node(bid, title, author, status)
        if self.head is None:
            self.head = newBook
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newBook
        print("book added successfully!")