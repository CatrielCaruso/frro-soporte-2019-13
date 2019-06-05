## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) .

from tkinter import *
from tkinter import ttk





class Listapais:

     def __init__(self):

        #Creo la ventana

        self.ventana=Tk()


        self.ventana.title("Ciudades de Argentina")
        self.ventana.iconbitmap("Screenshot_2019-06-03 UTN - Universidad Tecnologica Nacional Facultad Regional Rosario.ico")
        self.ventana.config(cursor="watch")
        self.ventana.config(bg="beige")
        self.ventana.geometry("500x300")

        #Creo el Arbol
        self.arbol=ttk.Treeview(self.ventana)
        self.arbol.pack( fill=BOTH, expand=False)



        #Cargo el arbol
        self.arbol.insert('', 'end', 'item0', text='Ciudades')

        self.arbol.insert('item0','0','item1',text='Rosario')
        self.arbol.insert('item0', '1', 'item2', text='Cordoba')
        self.arbol.insert('item0', '2', 'item3', text='Chalten')
        self.arbol.insert('item0', '3', 'item4', text='Ushuaia')
        self.arbol.insert('item0', '4', 'item5', text='Funes')

        self.arbol.insert('item1','end','dos1',text='CP 2000')
        self.arbol.insert('item2', 'end', 'dos2', text='CP 5000 ')
        self.arbol.insert('item3', 'end', 'dos3', text='CP 9301')
        self.arbol.insert('item4', 'end', 'dos4', text='CP V9410')
        self.arbol.insert('item5', 'end', 'dos5', text='CP S2132')
        self.arbol.config(height=15)



        self.ventana.mainloop()




listita=Listapais()