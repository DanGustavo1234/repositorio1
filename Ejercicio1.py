#Realice un programa que realice la sumatoria 
#de los números enteros comprendidos entre el 1 y el 10, es decir, 1 + 2 + 3 + …. + 10.

import sys
from tkinter import * 
import random

app = Tk()
app.title("Suma de numeros ")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

boton2 = Button(vp, text="enviar",command=lambda:sumatoria())
boton2.grid(column=1, row=6)

def sumatoria():
    cont=0
    for i in range(1,11):
        cont =cont+i
    etiqueta2.config(text="La sumatoria es {} ".format(cont))
   

    # El ciclo o bucle se detiene cuando el usuario adivina el número
    # correctamente y se muestra un mensaje final.

etiqueta3= Label(vp,text="Quieres saber la sumatoria de los numeros enteros entre el 1 y el 10 click aqui: ")
etiqueta3.grid(column=1, row=1, sticky=(W,E))       
etiqueta2 = Label(vp)
etiqueta2.grid(column=1, row=2, sticky=(W,E))







# El usuario adivina el número aleatorio generado por la computadora.
app.mainloop() 