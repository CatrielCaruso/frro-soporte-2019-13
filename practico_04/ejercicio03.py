## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) .

from tkinter import *





class Listapais:

     def __init__(self):

        #Creo la ventana

        self.ventana=Tk()
        self.ventana.geometry("600x450")
        self.ventana.title("Ciudades de Argentina")
        self.ventana.iconbitmap("Screenshot_2019-06-03 UTN - Universidad Tecnologica Nacional Facultad Regional Rosario.ico")


        self.ventana.config(cursor="watch")
        self.ventana.config(bg="beige")

        #Creo un label para nombrar a la lista
        self.nombre=Label(self.ventana,text="Ciudad:").place(x=100,y=100)
        self.nombre2 = Label(self.ventana, text="Código postal:").place(x=350, y=100)
        #Creo la lista


        self.lista = Listbox(self.ventana,width=40,selectforeground="#ffffff",
                                  selectbackground="#00aa00",
                                  selectborderwidth=5,activestyle=NONE,exportselection=False)
        self.lista.insert(0, "Rosario ")
        self.lista.insert(1, "Cordoba")
        self.lista.insert(2, "Funes")
        self.lista.insert(3, "Chalten")
        self.lista.insert(4, "Iruya")
        self.lista.insert(5, "Mar del Plata")

        self.lista.place(x=100, y=130)

        self.lista2 = Listbox(self.ventana, width=20, selectforeground="#ffffff",
                             selectbackground="#00aa00",
                             selectborderwidth=5, activestyle=NONE)

        self.lista2.insert(0, "2000 ")
        self.lista2.insert(1, "5000")
        self.lista2.insert(2, "2132")
        self.lista2.insert(3, "9301")
        self.lista2.insert(4, "4633")
        self.lista2.insert(5, "7600")

        self.lista2.place(x=350, y=130)






        self.ventana.mainloop()




listita=Listapais()