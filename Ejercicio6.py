# Escriba un programa que pida un año y que escriba si es bisiesto o no. Se recuerda que los años 
# bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.
import sys
from tkinter import * 
app = Tk()
app.title("Años Bisiestos")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(60,60), pady=(60,60))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

boton2 = Button(vp, text="enviar",command=lambda:años())
boton2.grid(column=1, row=2)

valor=''
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=1, row=1)

etiqueta= Label(vp,text="Ingrese un Año")
etiqueta.grid(column=0, row=1, sticky=(W,E))   

etiqueta1= Label(vp)
etiqueta1.grid(column=2, row=1, sticky=(W,E))   

def años():
     year=int(entrada_texto.get())
     if year % 4 == 0:
         if year % 100 == 0:
             if year % 400 == 0:
                  etiqueta1.config(text='El año es bisiesto')
             else:
                etiqueta1.config(text='El año no es bisiesto')
         else:
             etiqueta1.config(text='El año es bisiesto.')
     else: 
         etiqueta1.config(text='El año no es bisiesto.')



app.mainloop() 
