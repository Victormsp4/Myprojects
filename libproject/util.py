from random import randint
class biblioteca:
    #cria um obj biblioteca
    def __init__(self,nome,banco_livros):
        self.banco_livros = {}
        self.nome = nome
    
    #adiciona um livro, verifica se e uma instancia de string e padroniza em minuculo sem espaços
    def add_book(self,id,nome):
        if isinstance(name, str):
            name = name.strip().lower()
            if nome not in self.banco_livros:
                return self.banco_livros[id:nome].update()
  
    # gera um id unico para um novo livro
    def gera_id(self):
        getid = randint(1000,1999)
        if getid not in self.banco_livros:
            return getid
        else:
            print('ja ta la')
    
    def verifica(self, name):
            if isinstance(name, str):
                name = name.strip().lower()
                return name