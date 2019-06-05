## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 
from tkinter import *
from tkinter import ttk

root = Tk()
root.configure(background="white")
root.title("Lista de Ciudades")
root.geometry("200x300")
root.resizable(False, False)
# Centra la ventana.
root.geometry(
    "+{}+{}".format(
        int(root.winfo_screenwidth() / 2 - root.winfo_reqwidth() / 2),
        int(root.winfo_screenheight() / 2 - root.winfo_reqheight() / 2),
    )
)
root.protocol("WM_DELETE_WINDOW", lambda: closeWindow(root))


def closeWindow(window):
    window.destroy()
    window.quit()


def createControls():
    treeView = ttk.Treeview(root, show="tree")
    treeView.pack(fill="both", expand=True)
    item = treeView.insert("", END, text="Ciudades")
    subitem = treeView.insert(item, END, text="Armstrong")
    treeView.insert(subitem, END, text="CP 2508")
    subitem = treeView.insert(item, END, text="Buenos Aires")
    treeView.insert(subitem, END, text="CP 1000")
    subitem = treeView.insert(item, END, text="Córdoba")
    treeView.insert(subitem, END, text="CP 5000")
    subitem = treeView.insert(item, END, text="La Plata")
    treeView.insert(subitem, END, text="CP 1900")
    subitem = treeView.insert(item, END, text="Mar del Plata")
    treeView.insert(subitem, END, text="CP 7600")
    subitem = treeView.insert(item, END, text="Rosario")
    treeView.insert(subitem, END, text="CP 2000")


if __name__ == "__main__":
    createControls()
    root.mainloop()