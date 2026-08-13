books = []
def add_book():
    book_name = input('Enter the name of book you want to add : ')
    book_author = input('Enter the book author also : ')
    books.append([book_name, book_author])
def display_books():
    print('\n=====> Available Books <=====\n')
    for book_name, book_author in books:
        print(f'{book_name} : {book_author}')
def search_book():
    found = False
    search_book = input('Enter the book you want to search : ')
    for book_name, book_author in books:
        if book_name == search_book:
            print(f'{book_name} : {book_author}')
            found = True
    if not found:
        print('Book not found!')
def remove_book():
    found = False
    remove_book = input('Enter the book name you want to remove : ')
    for book_name, book_author in books:
        if book_name == remove_book:
            books.remove([book_name, book_author])
            found = True
    if not found:
        print('BOOK NOT FOUND!')

# main menu
while True:
    print('\n=====> Library Management System <=====\n')
    print('1.Add Book')
    print('2.Display Book')
    print('3.Search Book')
    print('4.Remove Book')
    print('5.Exit')
    try:
        choice = int(input('Enter your Choice : '))
        if choice == 1:
            add_book()
        elif choice == 2:
            display_books()
        elif choice == 3:
            search_book()
        elif choice == 4:
            remove_book()
        elif choice == 5:
            print('THANKS FOR THE USE!')
            break
        else:
            print('Invalid choice! Please select 1-5.')

    except ValueError:
        print('Please enter a valid number!')
    