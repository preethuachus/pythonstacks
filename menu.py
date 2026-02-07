# while True:
#     print("1.add\n2.mul\n3.div\n4.sub\n5.exit")
#     ch=int(input("enter a choice :"))

#     if ch==1:
#         a=int(input("enter a value :"))
#         b=int(input("enter a value :"))
#         print(a+b)

#     elif ch==2:
#         a=int(input("enter a value :"))
#         b=int(input("enter a value :"))
#         print(a*b)

#     elif ch==3:
#         a=int(input("enter a value :"))
#         b=int(input("enter a value :"))
#         print(a/b)

#     elif ch==4:
#         a=int(input("enter a value :"))
#         b=int(input("enter a value :"))
#         print(a-b)

#     elif ch==5:
#         break

#     else:
#         print("invalid")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 1. Library Management System (Dictionary + Menu)

# Question:
# Design a menu-driven Library Management System using a dictionary.
# The program should support the following operations:

# Add a new book with details: Book ID, Name, Author, Price, Publisher

# Display all books available in the library

# Update the price of an existing book using Book ID

# Delete a book using Book ID

# Exit the program

# Ensure that duplicate Book IDs are not allowed.


# library = {}

# while True:
#     print("1.Add \n2.Display \n3.Update \n4.Delete \n5.Exit")
#     ch = int(input("enter a value : "))

#     if ch == 1:
#         book_id = input("Book Id: ")

#         if book_id in library:
#             print("book id already exist")
#         else:
#             name = input("name: ")
#             author = input("author: ")
#             price = input("price: ")
#             publisher = input("publisher: ")

#             library[book_id] = [name, author, price, publisher]
#             print("book added")

#     elif ch == 2:
#         if not library:
#             print("no books available")
#         else:
#             for bid, data in library.items():
#                 print("id:", bid)
#                 print("name:", data[0])
#                 print("author:", data[1])
#                 print("price:", data[2])
#                 print("publisher:", data[3])
#                 print("----")

#     elif ch == 3:
#         book_id = input("enter book id: ")

#         if book_id in library:
#             new_price = input("new price: ")
#             library[book_id][2] = new_price
#             print("price updated")
#         else:
#             print("book not found")

#     elif ch == 4:
#         book_id = input("enter book id: ")

#         if book_id in library:
#             del library[book_id]
#             print("book deleted")
#         else:
#             print("book not found")

#     elif ch == 5:
#         print("exit")
#         break

#     else:
#         print("invalid choice")



books = []

while True:
    print("\n1.Add Book \n2.Display Book \n3.Update Price \n4.Delete Book \n5.Exit")
    ch = int(input("Enter choice: "))

    # 1. Add Book
    if ch == 1:
        book_id = input("Book ID: ")

        found = False
        for b in books:
            if b[0] == book_id:
                found = True
                break

        if found:
            print("Book ID already exists")
        else:
            name = input("Book Name: ")
            price = input("Price: ")
            author = input("Author Name: ")
            books.append([book_id, name, price, author])
            print("Book added")

    # 2. Display Book
    elif ch == 2:
        book_id = input("Enter Book ID: ")

        found = False
        for b in books:
            if b[0] == book_id:
                print("ID:", b[0])
                print("Name:", b[1])
                print("Price:", b[2])
                print("Author:", b[3])
                found = True
                break

        if not found:
            print("Book not found")

    # 3. Update Price
    elif ch == 3:
        book_id = input("Enter Book ID: ")

        found = False
        for b in books:
            if b[0] == book_id:
                new_price = input("New Price: ")
                b[2] = new_price
                print("Price updated")
                found = True
                break

        if not found:
            print("Book not found")

    # 4. Delete Book
    elif ch == 4:
        book_id = input("Enter Book ID: ")

        found = False
        for i in range(len(books)):
            if books[i][0] == book_id:
                del books[i]
                print("Book deleted")
                found = True
                break

        if not found:
            print("Book not found")

    # 5. Exit
    elif ch == 5:
        print("Exit")
        break

    else:
        print("Invalid choice")





  