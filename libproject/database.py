import sqlite3

class Database:
    def __init__(self,name='books.db'):
        self.name = name
        self._create_table()
        
    #internal method
    def _create_table(self):
        conn = self._connection()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

    #internal method  
    def _connection(self):
        return sqlite3.connect(self.name)

    def add_book(self,name):
        conn = self._connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (name) VALUES(?)",(name,))
        conn.commit()
        conn.close()
    
    def remove_book(self,id_book):
        self.id = id_book
        conn = self._connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = (?)",(id_book,))
        conn.commit()
        conn.close()
    
    def list_books(self):
        conn = self._connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books ")
        listalivros = cursor.fetchall()
        #interface.txt(f'Título{'id':>24}',96)
        #interface.linha(lenn = 30, color = 92)
        for indice,i in listalivros:
            print(f'{i} {indice:>{29-len(i)}}')
        conn.close()