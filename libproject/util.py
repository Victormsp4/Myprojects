from interface import *
from random import randint
class Biblioteca:

    #cria um obj biblioteca com atributo privado.
    def __init__(self,nome):
        self.__banco_livros = {}
        self.nome = nome

    def remove_book(self, name):
        #lista os livros disponiveis
        if name in self.__banco_livros['books']:
            txt(f'book {self.__banco_livros['books'][name]} selected',92)
            txt(f'1 - remove book\n2 - back to menu',97)
            opt = int(input('->'))

            if opt == 1:
                txt(f'Book {self.__banco_livros['books'][name]} removed successfully.',92)
                del self.__banco_livros['books'][name]

            elif opt == 2:
                return
            
        else:
            txt('book not found',91)
    
    #adiciona um livro, em um dicionario aninhado.
    def add_book(self,id,name):
        if 'books' not in self.__banco_livros:
            self.__banco_livros['books']={id:name}

        else:
            self.__banco_livros['books'].update({id:name})
        txt(f'Book {name} added successfully with ID: {id}',92)

    # gera um id unico para um novo livro
    def gera_id(self):
        while True:
            self.getid = randint(1000,1999)
            if self.getid not in self.__banco_livros:
                return self.getid
            else:
                continue
    
    def list_books(self):
        #percorre o dicionario em busca do nome do livro, e printa o id e o nome do livro.
        menu('Books in the Library:',96)
        for key, value in self.__banco_livros['books'].items():
            txt(f'Name: {value} - ID: {key}',93)
    
    def search_books(self,name):
        if name in self.__banco_livros['books'].values():
            menu('book(s) found',96)
            for key, value in self.__banco_livros['books'].items():
                if name == value:
                    txt(f'Name: {value} - ID: {key}',93)

        else:
            txt('book(s) not found',91)