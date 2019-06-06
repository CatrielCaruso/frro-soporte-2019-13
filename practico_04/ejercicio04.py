## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 
import tkinter as tk
from tkinter import ttk



class Formulario(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        #Datos de la ventana principal
        main_window.geometry("500x300")
        main_window.title("Ciudades de Argentina")
        main_window.iconbitmap("Screenshot_2019-06-03 UTN - Universidad Tecnologica Nacional Facultad Regional Rosario.ico")
        main_window.config(cursor="watch")
        main_window.config(bg="beige")
         #datos del arbol(Treeview), Descarte que inicie desde ciudad porque no podia configurarlo en el alta.
        self.arbol = ttk.Treeview(self)

        item = self.arbol.insert("", tk.END, text="Rosario")
        self.arbol.insert(item, tk.END, text=" CP 2000")
        item = self.arbol.insert("", tk.END, text="Cordoba")
        self.arbol.insert(item, tk.END, text="CP 5000")
        item = self.arbol.insert("", tk.END, text="Chalten")
        self.arbol.insert(item, tk.END, text="CP 9301")
        item = self.arbol.insert("", tk.END, text="Ushuaia")
        self.arbol.insert(item, tk.END, text="CP V9410")
        item = self.arbol.insert("", tk.END, text="Funes")
        self.arbol.insert(item, tk.END, text="CP S2122")
        self.arbol.pack()

        self.pack()


main_window = tk.Tk()
form = Formulario(main_window)

#funciones
'''Alta'''
def formulario_alta():
    new_ventana = tk.Toplevel(main_window)
    main_window.iconify()
    var_ciudad = tk.StringVar()
    var_CP = tk.StringVar()
    label = tk.Label(new_ventana, text="Ciudad: ")
    label2 = tk.Label(new_ventana, text="Código Postal: ")
    label.grid(column=1, row=1, padx=(50,50), pady=(10,10))
    label2.grid(column=2, row=1, padx=(40,40), pady=(10,5))


    Ciudad = tk.Entry(new_ventana,textvariable=var_ciudad)
    Ciudad.grid(column=1, row=2, padx=(5,5), pady=(10,5))
    CP = tk.Entry(new_ventana,textvariable=var_CP)
    CP.grid(column=2, row=2, padx=(5,5), pady=(10,5))

    btn_alta = tk.Button(new_ventana, text="Añadir")
    btn_alta.grid(column=3, row=2, padx=(50,50), pady=(10,10))
    def alta(event):
        item = form.arbol.insert("", tk.END, text=Ciudad.get())
        form.arbol.insert(item, tk.END, text=CP.get())
        main_window.deiconify()

    btn_alta.bind("<Button-1>", alta)

ancho_boton = 11
alto_boton = 3
btn_frm_alta = tk.Button(main_window, bg='DarkSeaGreen1', text="ALTA",width=ancho_boton,height=alto_boton, command=formulario_alta)
btn_frm_alta.place(x=400,y=80)



'''Baja'''
def baja():
    dev_item = form.arbol.focus()
    form.arbol.delete(dev_item)


ancho_boton = 11
alto_boton = 3
btn_baja = tk.Button(main_window, bg='DarkSeaGreen1', text="BAJA",width=ancho_boton,height=alto_boton, command=baja)
btn_baja.place(x=400,y=0)


'''Modificación'''
def formulario_modificacion():
    new_ventana = tk.Toplevel(main_window)
    main_window.iconify()
    elem = form.arbol.focus()
    elem_child = form.arbol.get_children(elem)
    var_ciudad = tk.StringVar(new_ventana, value=form.arbol.item(elem)['text'])

    var_CP = tk.StringVar(new_ventana, value=form.arbol.item(elem_child)['text'])
    label = tk.Label(new_ventana, text="Ciudad: ")
    label2 = tk.Label(new_ventana, text="Código Postal: ")
    label.grid(column=1, row=1, padx=(50,50), pady=(10,10))
    label2.grid(column=2, row=1, padx=(40,40), pady=(10,5))


    Ciudad = tk.Entry(new_ventana,textvariable=var_ciudad)
    Ciudad.grid(column=1, row=2, padx=(5,5), pady=(10,5))
    CP = tk.Entry(new_ventana,textvariable=var_CP)
    CP.grid(column=2, row=2, padx=(5,5), pady=(10,5))

    btn_alta = tk.Button(new_ventana, text="Modificar")
    btn_alta.grid(column=8, padx=(50,50), pady=(10,10), row=2)
    def modificacion(event):
        form.arbol.item(elem,text=Ciudad.get())
        form.arbol.item(elem_child,text=CP.get())
        main_window.deiconify()

    btn_alta.bind("<Button-1>", modificacion)
ancho_boton = 11
alto_boton = 3
btn_frm_alta = tk.Button(main_window, bg='DarkSeaGreen1', text="MODIFICAR",width=ancho_boton,height=alto_boton, command=formulario_modificacion)
btn_frm_alta.place(x=400,y=170)

form.mainloop()