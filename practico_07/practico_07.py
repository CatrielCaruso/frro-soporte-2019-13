"""Tp7 – Capa Presentacion Socios

Crear en Python usando Tkinter un formulario para gestionar los datos de Socios usando la Clase de la Capa de Negocio Socios .

El Formulario principal tiene que mostrar todos los socios en Treeview y tener los siguientes botones Alta , Baja , Modificar .

Apretar el Boton Alta se tiene que abrir un formulario con los campos para ingresar los datos de socio .
Incluye  2 botones Guardar y Cancelar.

Apretar el Boton Baja se tiene que dar de baja el socio seleccionado .

Apretar el Boton Modificar se tiene que abrir un formulario con los campos con los datos del socio seleccionado .
Incluye 2 botones Aceptar y Cancelar . """

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio
from tkinter import *
from tkinter import ttk
from enum import Enum

# CREACION DE LA VENTANA

ventana = Tk()
ventana.configure(background="snow")
ventana.title("ABM Socios")
ventana.geometry("500x500")
ventana.resizable(0, 0)
#  Frame


marco = Frame(ventana)
marco.grid(column=0, row=0, padx=(10,10), pady=(1,1))
boton = Frame(ventana, width=52)
boton.grid(column=0, row=1, padx=(10,10), pady=(1,1))
# Para centrar la ventana ventana.


ventana.geometry(
    "+{}+{}".format(
        int(ventana.winfo_screenwidth() / 2 - ventana.winfo_reqwidth() / 2),
        int(ventana.winfo_screenheight() / 2 - ventana.winfo_reqheight() / 2),
    )
)
ventana.protocol("WM_DELETE_WINDOW", lambda: close_window(ventana))


# Clase para las opciones
class Opciones(Enum):
    ALTA = 1
    BAJA = 2
    MODIFICACION = 3

id_socio_seleccionado = IntVar()

def close_window(window):
    window.destroy()
    window.quit()

def create_controls():
    get_socios()

def get_socios():
    add_data_to_table()

def add_data_to_table():
    delete_frame_grid_controls()
    ns = NegocioSocio()
    global socios
    global id_socio_seleccionado
    socios = ns.todos()
    cont = 0
    Label(marco,text="", width=4, anchor="center", relief="ridge", font=("Helvetica", 12,)).grid(row=cont,column=0)
    Label(marco,text="DNI", width=10, anchor="center", relief="ridge", font=("Helvetica", 12,)).grid(row=cont,column=1)
    Label(marco,text="Nombre", width=20, anchor="center", relief="ridge", font=("Helvetica", 12)).grid(row=cont,column=2)
    Label(marco,text="Apellido", width=20, anchor="center", relief="ridge", font=("Helvetica", 12)).grid(row=cont,column=3)
    cont +=1
    for socio in socios:
        Radiobutton(marco, width=2, anchor="center", bg="white", relief="ridge", variable=id_socio_seleccionado, value=socio.id_socio).grid(row=cont,column=0)
        Label(marco,text=socio.dni, width=10, anchor="w", bg="white", relief="ridge", font=("Helvetica", 12)).grid(row=cont,column=1)
        Label(marco,text=socio.nombre, width=20, anchor="w", bg="white", relief="ridge", font=("Helvetica", 12)).grid(row=cont,column=2)
        Label(marco,text=socio.apellido, width=20, anchor="w", bg="white", relief="ridge", font=("Helvetica", 12)).grid(row=cont,column=3)
        cont +=1
    create_buttons(cont)

def delete_frame_grid_controls():
    list = marco.grid_slaves()
    for l in list:
        l.destroy()

def create_buttons(cont):
    Button(boton, text="Crear", width=10, anchor="center", padx=5, command=lambda:add_or_update_socio(Opciones.ALTA)).grid(row=0,column=0)
    Button(boton, text="Modificar", width=10, anchor="center", padx=5, command=lambda:add_or_update_socio(Opciones.MODIFICACION)).grid(row=0,column=1)
    Button(boton, text="Eliminar", width=10, anchor="center", padx=5, command=delete_socio).grid(row=0,column=2)
    Button(boton, text="Actualizar", width=10, anchor="center", padx=5, command=add_data_to_table).grid(row=0,column=3)

def add_or_update_socio(opcion):
    win = Toplevel()
    win.configure(background="white")
    win.geometry("240x130")
    win.resizable(0, 0)
    win.geometry(
        "+{}+{}".format(
            int(win.winfo_screenwidth() / 2 - win.winfo_reqwidth() / 2),
            int(win.winfo_screenheight() / 2 - win.winfo_reqheight() / 2),
        )
    )

    def aceptar(opcion):
        if opcion == Opciones.ALTA:
            add_socio(dni_socio.get(), nombre_socio.get(), apellido_socio.get())
        else:
            update_socio(socio, dni_socio.get(), nombre_socio.get(), apellido_socio.get())
        win.destroy()
        add_data_to_table()
        ventana.deiconify()

    def cancelar():
        win.destroy()
        ventana.deiconify()

    dni_socio = IntVar()
    nombre_socio= StringVar()
    apellido_socio = StringVar()

    if opcion == Opciones.MODIFICACION:
        ns = NegocioSocio()
        socio = ns.buscar(id_socio_seleccionado.get())
        if socio == None:
            cancelar()
        win.title("Modificar socio")
        dni_socio.set(socio.dni)
        nombre_socio.set(socio.nombre)
        apellido_socio.set(socio.apellido)
    elif opcion == Opciones.ALTA:
        win.title("Crear socio")

    Label(win, text="DNI", bg="white").grid(
        sticky=W + N + S, column=0, row=0, padx=5, pady=5
    )
    Entry(win, textvariable=dni_socio, bg="white").grid(
        sticky=E + N + S, column=1, columnspan=2, row=0, padx=5, pady=5
    )
    Label(win, text="Nombre", bg="white").grid(
        sticky=W + N + S, column=0, row=1, padx=5, pady=5
    )
    Entry(win, textvariable=nombre_socio, bg="white").grid(
        sticky=E + N + S, column=1, columnspan=2, row=1, padx=5, pady=5
    )
    Label(win, text="Apellido", bg="white").grid(
        sticky=W + N + S, column=0, row=2, padx=5, pady=5
    )
    Entry(win, textvariable=apellido_socio, bg="white").grid(
        sticky=E + N + S, column=1, columnspan=2, row=2, padx=5, pady=5
    )
    Button(
        win,
        text="Aceptar",
        bg="white",
        command=lambda: aceptar(opcion),
        height=1,
        width=5,
    ).grid(column=1, row=3, padx=5, pady=5, sticky=W + E + N + S)
    Button(
        win,
        text="Cancelar",
        bg="white",
        command=lambda: cancelar(),
        height=1,
        width=5,
    ).grid(column=2, row=3, padx=5, pady=5, sticky=W + E + N + S)

def add_socio(dni, nombre, apellido):
    socio = Socio(dni=dni, nombre=nombre, apellido=apellido)
    ns = NegocioSocio()
    ns.alta(socio)

def update_socio(socio, dni, nombre, apellido):
    socio.dni = dni
    socio.nombre = nombre
    socio.apellido = apellido
    ns = NegocioSocio()
    ns.modificacion(socio)

def delete_socio():
       ns = NegocioSocio()
       global id_socio_seleccionado
       ns.baja(id_socio_seleccionado.get())
       add_data_to_table()

if __name__ == "__main__":
    create_controls()
    ventana.mainloop()



