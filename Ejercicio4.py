#Escriba un programa que pida dos números enteros y que calcule su división,
#escribiendo si la división es exacta o no
import sys
from tkinter import * 
import random

app = Tk()
app.title("Division")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

boton2 = Button(vp, text="enviar",command=lambda:perimetro_area())
boton2.grid(column=3, row=4)

valor2=''
entrada_texto2 = Entry(vp, width=10, textvariable=valor2)
entrada_texto2.grid(column=2, row=3)

valor=''
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=7, row=3)


etiqueta= Label(vp,text="Numero 1")
etiqueta.grid(column=0, row=3, sticky=(W,E))       

etiqueta1 = Label(vp,text="Numero 2")
etiqueta1.grid(column=3, row=3, sticky=(W,E))

etiqueta2 = Label(vp)
etiqueta2.grid(column=11, row=3, sticky=(W,E))




def perimetro_area():
     x=int(entrada_texto2.get())
     y=int(entrada_texto.get())
     div=x/y
     if x%y != 0:
         etiqueta2.config(text="La division no es exacta {} ".format(div))
     else:
        etiqueta2.config(text="La division  es exacta {} ".format(int(div)))
     

app.mainloop() 


