## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 
from tkinter import *
from tkinter import ttk





class Listapais:

     def __init__(self):

        #Creo la ventana

        self.ventana=Tk()


        self.ventana.title("Ciudades y su código postal de Argentina")
        self.ventana.iconbitmap("Screenshot_2019-06-03 UTN - Universidad Tecnologica Nacional Facultad Regional Rosario.ico")
        self.ventana.config(cursor="watch")
        self.ventana.config(bg="beige")
        self.ventana.geometry("500x350")



        #Creo el Arbol
        self.arbol=ttk.Treeview(self.ventana)
        self.arbol.pack( )
        # Creo botones
        self.ancho_boton = 11
        self.alto_boton = 3
        self.boton1 = Button(self.ventana,width=self.ancho_boton,height=self.alto_boton, text="Insert")
        self.boton1.place(x=400,y=10)
        self.boton2 = Button(self.ventana,width=self.ancho_boton,height=self.alto_boton, text="Delete")
        self.boton2.place(x=400, y=135)
        self.boton3 = Button(self.ventana,width=self.ancho_boton,height=self.alto_boton, text="Update")
        self.boton3.place(x=400, y=260)

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


def main():
   mi_app = Listapais()
   return 0


if __name__ == '__main__':
   main()






