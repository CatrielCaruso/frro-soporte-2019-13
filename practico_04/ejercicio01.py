## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 . 
 
from tkinter import *


def suma():
    suma=float(entrada1.get())+ float(entrada2.get())
    return var.set(suma)

def resta():
    resta=float(entrada1.get())- float(entrada2.get())
    return var.set(resta)

def multiplicacion():
    multiplicacion=float(entrada1.get())*float( entrada2.get())
    return var.set(round(multiplicacion,3))

def dividir():
    dividir=float(entrada1.get())/float( entrada2.get())
    return var.set(dividir)



ventana = Tk()
ventana.geometry('700x200')
ventana.configure(bg='azure2')
ventana.title('Calculadora')
var = StringVar()
numero1 = Label(text="Primer operando", font=("Agency FB", 14), bg="ghost white")
numero1.place(x=60, y=40)
entrada1 = Entry(ventana)
entrada1.place(x=60, y=80)

numero2 = Label(text="Segundo operando", font=("Agency FB", 14), bg="ghost white")
numero2.place(x=300, y=40)
entrada2 = Entry(ventana)
entrada2.place(x=300, y=80)

botonsuma = Button(ventana, text="+", command=suma)
botonsuma.place(x=451,y=75)

botonresta = Button(ventana, text="-", command=resta)
botonresta.place(x=469,y=75)

botonmultiplicacion = Button(ventana, text="x", command=multiplicacion)
botonmultiplicacion.place(x=484,y=75)

botondividir = Button(ventana, text="/", command=dividir)
botondividir.place(x=499,y=75)

res = Label(bg="azure2", textvariable=var)
res.place(x=250,y=120)

ventana.mainloop()




