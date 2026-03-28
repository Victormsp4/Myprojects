from tkinter import Tk,Frame,Button,Label,Entry,Scrollbar
from tkinter import ttk
from database import Database


"""def menu(title,cor):
    print('-'*(len(title)+6))
    print(f'\033[{cor}m{title:^{len(title)+6}}\033[0m')
    print('-'*(len(title)+6))

def linha(lenn = 30, color = 96):
    print(f'\033[{color}m-\033[0m'*lenn)

def txt(txt,cor):
    print(f'\033[{cor}m{txt}\033[0m')"""



class MyWindows:
    def __init__(self, obj_banco):
        self.db = obj_banco
        self.window = Tk()
        self._screen()
        self.screen_frames()
        self.list_frame2()
        self.popular()
        self.window.mainloop()
        
    #internal method
    def _screen(self):
        self.window.title('Library Management System')
        self.window.configure(background='steelblue')
        self.window.geometry('800x600')#tamanho inicial da tela
        self.window.maxsize(height=1080,width=1920)#tamanho maximo
        self.window.minsize(height=300, width=400)#tamanho minimo
        self.window.resizable(True,True)#para responsividade, em caso de false a tela fica travada no tamanho inicial, valores default são True
    
    def screen_frames(self):
        self.frame_1 = Frame(self.window, bd = 5,relief = 'sunken', bg = 'gray90')
        self.frame_1.place(relx = 0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.label = Label(self.frame_1,relief='groove', anchor='nw', text='Gestão de Livros', bg = 'gray99')
        self.label.place(relx = 0.06, rely=0.1, relwidth=0.70, relheight=0.75)

        #entre add_button
        self.entre = Entry(self.label,bd=3, relief='groove')
        self.entre.place(relx = 0.20, rely=0.12, relwidth=0.70, relheight=0.15)

        #entre remove
        self.entre2 = Entry(self.label,bd=3, relief='groove')
        self.entre2.place(relx = 0.20, rely=0.29, relwidth=0.15, relheight=0.15)

        #add button
        self.button = Button(self.label, text='Adicionar', command = self.add_book)
        self.button.place(relx = 0.02, rely=0.12, relwidth=0.15, relheight=0.15)

        #limpar button
        self.delete_buton = Button(self.label, text = "Limpar", command = self.limpacampo)
        self.delete_buton.place(relx = 0.02, rely=0.80, relwidth=0.15, relheight=0.15)
        
        #remeve button
        self.remove_book_button = Button(self.label, text = 'Remover', command = self.remove_book)
        self.remove_book_button.place(relx = 0.02, rely=0.28, relwidth=0.15, relheight=0.15)

        ########################
        self.frame_2 = Frame(self.window, bd = 5,relief = 'sunken', bg = 'gray90')
        self.frame_2.place(relx = 0.02, rely=0.5, relwidth=0.96, relheight=0.46)



    def list_frame2(self):
        #style altera o tema do Treeview que por padrão e o do windows
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading', background = "#D3D3D3", relief = 'groove')
        #função para mostrar uma lista
        self.list_frame_books = ttk.Treeview(self.frame_2, columns=('livros', 'id'))
        self.list_frame_books.heading('#0', text = '')
        self.list_frame_books.heading('#1', text = 'Livros')
        self.list_frame_books.heading('#2', text = 'Id')

        self.list_frame_books.column('#0', width=1)
        self.list_frame_books.column('#1', width=245)
        self.list_frame_books.column('#2', width=245)
        self.list_frame_books.place(relx = 0.1, rely=0.1, relwidth=0.80, relheight=0.80)

        self.scroll_lista = Scrollbar(self.list_frame_books, orient='vertical')
        #definindo Scrollbar para funcionar dentro do Treeview
        self.list_frame_books.configure(yscroll = self.scroll_lista.set)
        self.scroll_lista.place(relx = 0.978, rely=0.15, relwidth=0.02, relheight=0.80)

    def limpacampo(self):
        self.entre.delete(0,'end')
        self.entre2.delete(0,'end')

    def add_book(self):
        date_entry = self.entre.get()
        self.db.add_book(date_entry)
        self.limpacampo()
        self.popular()
    
    def remove_book(self):
        id_book_remove = self.entre2.get()
        self.db.remove_book(id_book_remove)
        self.limpacampo()
        self.popular()


    def list_book(self):
        pass

    def popular(self):
        self.list_frame_books.delete(*self.list_frame_books.get_children())
        conn = self.db._connection()
        cursor = conn.cursor()
        vquery = cursor.execute("SELECT name, id FROM books ORDER BY name ASC;")
        for i in vquery:
            self.list_frame_books.insert("", "end",values=i)


#injeção de dependencia
minhajanela = MyWindows(Database())
