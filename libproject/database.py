import sqlite3
import interface
class Database:
    def __init__(self,name='books.db'):
        self.name = name
    
    #internal method
    def _connection(self):
        return sqlite3.connect(self.name)

    def addbook(self,name):
        conn = self._connection()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
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
        interface.txt('Título   |   id',96)
        interface.linha(lenn = 20, color = 92)
        for indice,i in listalivros:
            print(f'{i} {indice:>{14-len(i)}}')
        conn.close()