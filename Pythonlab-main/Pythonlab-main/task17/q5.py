'''write a python program that allow a liebririan to add several book to a library .for each book, ask the user
to enter its tittle and number of copeis , store each book and its avialable copy count in a dictioary
.
after the book added, displayed and a menu that lets the user issue a book,return a book display a book ore
exit a program
conditios:
1. book  title should e compared without distinguisly uppercase and lowercase a letter.
2. a book can be issued only if it is exist in the library and at least one copy is available
3. issuing a book decrease its avaiable copy count by one 
4. a book can be returbned only if it exist in the library and at least oe copy is alredy issued.
5. returning a book decrease its available copy count by one.
6. display an appropraite message for an available book , an invalid choice or an invalid no. of copies'''


# solution:

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, copies):
        key = title.lower()
        self.books[key] = [title, copies, copies]
        def issue_book(self, title):
        key = title.lower()
        if key not in self.books:
            print("Book not found.")
        elif self.books[key][1] == 0:
            print("No copies are available.")
        else:
            self.books[key][1] -= 1
            print("Book issued successfully.")

    def return_book(self, title):
        key = title.lower()
        if key not in self.books:
            print("Book not found.")
        elif self.books[key][1] == self.books[key][2]:
            print("No copy of this book is currently issued.")
        else:
            self.books[key][1] += 1
            print("Book returned successfully.")

    def display_books(self):
        print("\nLibrary Books:")
        for details in self.books.values():
            title = details[0]
            available_copies = details[1]
            print(title, "- Available copies:", available_copies)


library = Library()
number_of_books = int(input("How many different books do you want to add? "))

for i in range(number_of_books):
    title = input("Enter book title: ").strip()
    copies = int(input("Enter number of copies: "))

    if copies <= 0:
            print("Number of copies must be greater than zero.")
    else:
            library.add_book(title, copies)
            print("Book added successfully.")

while True:
    print("\n1. Issue a book")
    print("2. Return a book")
    print("3. Display all books")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the title of the book to issue: ").strip()
        library.issue_book(title)

    elif choice == "2":
        title = input("Enter the title of the book to return: ").strip()
        library.return_book(title)

    elif choice == "3":
        library.display_books()

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")




