from time import sleep
from util import *
from interface import *


library = Biblioteca('Central Library')
menu('Welcome to the Library Management System')
while True:
    options = ['Add Book', 'Remove Book', 'Search Book', 'Exit']
    linha()
    for i, options in enumerate(options):
        print(f'{i+1} {options}')
    linha()
    opt = int(input('->'))

    if opt == 1:
        nome = str(input('Enter the name of the book: '))
        library.add_book(library.gera_id(),nome)
        continue

    if opt == 2:
        pass

    if opt == 3:
        library.list_books()
        name = input('select a book or "@" for exit: ')
        if name == '@':
            continue
        library.get_books(name)

    if opt == 4:
        print('Exiting the program...')
        sleep(0.7)
        break