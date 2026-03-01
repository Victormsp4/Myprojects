from random import randint
class Biblioteca:
    #cria um obj biblioteca
    def __init__(self,nome):
        self.banco_livros = {}
        self.nome = nome

    def remove_book(self):
        pass
    
    #adiciona um livro.
    def add_book(self,nome,id):
        self.banco_livros.update({id:nome})
        print('\033[92mBook added successfully!\033[0m')
  
    # gera um id unico para um novo livro
    def gera_id(self):
        while True:
            self.getid = randint(1000,1999)
            if self.getid not in self.banco_livros:
                return self.getid
            else:
                continue

    #exibi o dicionario de livros
    def list_books(self):
        print(self.banco_livros)
    
    def get_books(self, name):
        if name in self.banco_livros:
            print(f'\033[92mbook {name} selected\033[0m')
            print(f'1 - remove book\n2 - back to menu')
            opt = int(input('->'))
            if opt == 1:
                del self.banco_livros[name]
                print(f'\033[92mbook {name} removed successfully!\033[0m')
            elif opt == 2:
                return
        else:
            print('book not found')