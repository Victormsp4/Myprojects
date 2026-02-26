from util import *
from interface import *


options = ['Add Book', 'Remove Book', 'Search Book', 'Exit']
menu('Welcome to the Library Management System')
linha()
for i, opt in enumerate(options):
    print(f'{i+1} {opt}')
linha()
opt = int(input(""))
