## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 
from tkinter import *
from math import *


'''Caracteristicas de la interfaz'''
ventana=Tk()
ventana.geometry("400x600")
ventana.resizable(False, False)
ventana.config(relief="groove")
ventana.config(cursor="mouse")
ventana.config(bg="beige")
ventana.title('CALCULADORA')
ventana.iconbitmap("Screenshot_2019-06-03 UTN - Universidad Tecnologica Nacional Facultad Regional Rosario.ico")

'''Funciónes'''
def btnClik(num):
 global operador
 operador = operador + str(num)
 var1.set(operador)

def operacion():
 global operador
 try:
    opera = str(eval(operador))
 except:
     clear()
     opera=("ERROR")


 var1.set(opera)

def clear():
    global operador
    operador=("")
    var1.set(operador)

'''Variables'''

var1 = StringVar()
operador = ""
'''Es la función que cree arriba para que limpie la pantalla'''
clear()
'''Declaro y le doy valor a estas variables para los tamaños de los botones'''
ancho_boton = 11
alto_boton = 3

'''Programo los botones'''
boton1=Button(ventana, text=' + ',width=ancho_boton,height=alto_boton,command=lambda :btnClik("+")).grid(row=1, column=4)
boton2=Button(ventana, text=' - ',width=ancho_boton,height=alto_boton,command=lambda :btnClik("-")).grid(row=2, column=4)
boton3=Button(ventana, text=' / ',width=ancho_boton,height=alto_boton,command=lambda :btnClik("/")).grid(row=3, column=4)
boton4=Button(ventana, text=' x ',width=ancho_boton,height=alto_boton,command=lambda :btnClik("x")).grid(row=4, column=4)
boton5=Button(ventana, text=' 7 ',width=ancho_boton,height=alto_boton,command=lambda :btnClik(7)).grid(row=1, column=1)
boton6=Button(ventana, text=' 8 ',width=ancho_boton,height=alto_boton,command=lambda :btnClik(8)).grid(row=1, column=2)
boton7=Button(ventana, text=' 9 ',width=ancho_boton,height=alto_boton,command=lambda :btnClik(9)).grid(row=1, column=3)
boton8=Button(ventana, text=' 4 ',width=ancho_boton,height=alto_boton,command=lambda :btnClik(4)).grid(row=2, column=1)
boton9=Button(ventana, text=' 5 ',width=ancho_boton,height=alto_boton,command=lambda :btnClik(5)).grid(row=2, column=2)
boton10=Button(ventana, text=' 6 ',width=ancho_boton,height=alto_boton,command=lambda :btnClik(6)).grid(row=2, column=3)
boton11=Button(ventana, text=' 1 ',width=ancho_boton,height=alto_boton,command=lambda :btnClik(1)).grid(row=3, column=1)
boton12=Button(ventana, text=' 2 ',width=ancho_boton,height=alto_boton,command=lambda :btnClik(2)).grid(row=3, column=2)
boton13=Button(ventana, text=' 3 ',width=ancho_boton,height=alto_boton,command=lambda :btnClik(3)).grid(row=3, column=3)
boton14=Button(ventana, text=' 0 ',width=ancho_boton,height=alto_boton,command=lambda :btnClik(0)).grid(row=4, column=1)
boton15=Button(ventana, text='=',width=ancho_boton,height=alto_boton,command=operacion).grid(row=4, column=2, columnspan=2, sticky=W + E)

''' Creo y programo la entrada de datos '''
entrada = Entry(ventana,bd="30",bg="snow",width="100",borderwidth=25,textvariable=var1)
entrada.grid(row=0, column=0, columnspan=6,sticky=W + E, padx=0, pady=100)
entrada.config(width="40",insertwidth=4)

ventana.mainloop()














