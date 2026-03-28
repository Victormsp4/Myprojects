from tkinter import Tk, ttk, Frame, Label, Scrollbar, Entry, Button

window = Tk()

#configurando a janela
window.geometry('300x400')
window.resizable(False, False)

#labem
frame1 = Frame(window, bd = 2 , relief= 'groove')
frame1.place(relx=0.05, rely = 0.05, relwidth = 0.9, relheight=0.9)

#frame
label1 = Label(window, text='Program Crack')
label1.place(relx=0.06, rely = 0.06, relwidth = 0.3, relheight=0.039)

#button
button = Button(frame1, text='Get')
button.place(relx=0.1, rely = 0.1, relwidth = 0.2, relheight=0.06)

#entry
entry = Entry(frame1)
entry.place(relx=0.3, rely = 0.1, relwidth = 0.5, relheight=0.06)

#treeview
treeview = ttk.Treeview(frame1, columns=('views'))

treeview.heading('#0', text='')
treeview.heading('#1', text='views')
treeview.column('#0', width=10)
treeview.column('#1', width=200)
treeview.place(relx=0.06, rely = 0.50, relwidth = 0.88, relheight=0.40)

window.mainloop()