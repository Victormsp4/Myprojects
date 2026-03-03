from random import randint
class Biblioteca:

    #cria um obj biblioteca com atributo privado.
    def __init__(self,nome):
        self.__banco_livros = {}
        self.nome = nome

    def remove_book(self, name):
        Biblioteca.get_books(self)
        if name in self.__banco_livros['books']:
            print(f'\033[95mbook {name} selected\033[0m')
            print(f'1 - remove book\n2 - back to menu')
            opt = int(input('->'))
            if opt == 1:
                del self.__banco_livros['books'][name]
                print(f'\033[92mbook {name} removed successfully!\033[0m')
            elif opt == 2:
                return
        else:
            print('book not found')
    
    #adiciona um livro, em um dicionario aninhado.
    def add_book(self,nome,id):
        if 'books' not in self.__banco_livros:
            self.__banco_livros['books']={id:nome}
        else:
            self.__banco_livros['books'].update({id:nome})
        print('\033[92mBook added successfully!\033[0m')
  
    # gera um id unico para um novo livro
    def gera_id(self):
        while True:
            self.getid = randint(1000,1999)
            if self.getid not in self.__banco_livros:
                return self.getid
            else:
                continue
    
    def get_books(self):
        for key,value in self.__banco_livros['books'].items():
            print(f'\033[92m{key}, \033[91m{value}\033[0m')
