from abc import ABC, abstractmethod

# The ItemLibrary class is the superclass for Book, Magazine and DVD.
class ItemLibrary(ABC):
    def __init__(self, item):
        self.item = item

    # The abstract method 'borrow' must be implemented by all subclasses.
    @abstractmethod
    def loan(self) -> bool:
        ...

# The class book inherits from ItemLibrary and implements the method 'borrow'.
class Book(ItemLibrary):
    def loan(self) -> bool:
        print(f"book to loan... - {self.item}")
        return True

# The class magazine inherits from ItemLibrary and implements the method 'borrow'.
class Magazine(ItemLibrary):
    def loan(self) -> bool:
        print(f"Magazine to loan... - {self.item}")
        return True

# The class DVD inherits from ItemLibrary and implements the method 'borrow'.
class DVD(ItemLibrary):
    def loan(self) -> bool:
        print(f"DVD to loan... - {self.item}")
        return True

# the function confirms whether the item has been borrowed or not
def make_loan(itemlibrary: ItemLibrary):
    item_loan = itemlibrary.emprestar()

    if item_loan:
        print("Item loan")

    else:
        print("Item NOT loan")    

book = Book("Habitos Atomicos")
make_loan(book)        

magazine = Magazine("newspaper")
make_loan(magazine)

dvd = DVD("Miranha 2")
make_loan(dvd)

