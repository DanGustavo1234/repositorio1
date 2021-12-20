#Leer un numero entre 1 y 20 e imprimir
#su equivalente en números romanos.

import sys
from tkinter import * 
import random

app = Tk()
app.title("Numeros enteros a romanos")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

boton2 = Button(vp, text="enviar",command=lambda:sumatoria())
boton2.grid(column=1, row=6)
valor2=''
entrada_texto2 = Entry(vp, width=10, textvariable=valor2)
entrada_texto2.grid(column=1, row=5)

def sumatoria():
     x=int(entrada_texto2.get())
     if x>=1 and x<=20:
          numeros_romanos=["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII","XIV","XV","X",
         "VI","XVII","XVIII","XIX","XX"]
     t=(numeros_romanos[x-1])
     etiqueta2.config(text="El numero en romano es {}".format(t))

  

etiqueta3= Label(vp,text="Ingrese un numero entre el 1 y 20 se lo mostrara en numeros romanos ")
etiqueta3.grid(column=1, row=1, sticky=(W,E))       
etiqueta2 = Label(vp)
etiqueta2.grid(column=1, row=2, sticky=(W,E))


app.mainloop() 
