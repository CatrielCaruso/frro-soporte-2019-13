"""Tp7 – Capa Presentacion Socios

Crear en Python usando Tkinter un formulario para gestionar los datos de Socios usando la Clase de la Capa de Negocio Socios .

El Formulario principal tiene que mostrar todos los socios en Treeview y tener los siguientes botones Alta , Baja , Modificar .

Apretar el Boton Alta se tiene que abrir un formulario con los campos para ingresar los datos de socio .
Incluye  2 botones Guardar y Cancelar.

Apretar el Boton Baja se tiene que dar de baja el socio seleccionado .

Apretar el Boton Modificar se tiene que abrir un formulario con los campos con los datos del socio seleccionado .
Incluye 2 botones Aceptar y Cancelar . """

from tkinter import *

# Creacion de la ventana principal

ventana = Tk()
ventana.geometry('700x500')
ventana.configure(bg="SlateGray3" )
ventana.title('ABM Socios')
ventana.resizable(0, 0)

# Creación del frame

marco=Frame()
marco.pack()
marco.config(bg="ghost white")
marco.config(width="650", height="450")
ventana.mainloop()