from time import sleep
from database import *
from interface import *


database = Database('books.db')
menu('Welcome to the Library Management System',96)
while True:
    try:
        options = ['Add Book', 'Remove Book', 'Search Book', 'Exit']
        linha()
        for i, options in enumerate(options):
            print(f'{i+1} {options}')
        linha()
        opt = int(input('->'))

        if opt == 1:
            nome = str(input('Enter the name of the book: '))
            if nome.strip() == '':
                txt('Book name cannot be empty. Please try again.',91)
                continue
            database.addbook(nome)

        if opt == 2:
            database.list_books()
            book_id = int(input('selection a book ID:'))
            database.remove_book(book_id)

        if opt == 3:
            #name = input('Enter the name of the book to search: ')
            database.list_books()
            sleep(0.7)

        if opt == 4:
            print('Exiting the program...')
            sleep(0.7)
            break
    except ValueError:
        txt('Invalid option, please enter a number between 1 and 3 or 4 for exit.',91)
        continue
    except KeyError:
        txt('There are no books registered in the library.',91)
        continue
    except (TypeError, NameError):
        txt('Error occurred while processing the book information. Please try again.',91)