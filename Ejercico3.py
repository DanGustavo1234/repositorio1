#Hallar el perímetro y el área de un rectángulo ingresando la base b y la altura h

import sys
from tkinter import * 
import random

app = Tk()
app.title("Perimetro y area de un rectangulo ")

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


etiqueta= Label(vp,text="Base")
etiqueta.grid(column=0, row=3, sticky=(W,E))       

etiqueta1 = Label(vp,text="Altura")
etiqueta1.grid(column=3, row=3, sticky=(W,E))

etiqueta2 = Label(vp)
etiqueta2.grid(column=11, row=3, sticky=(W,E))




def perimetro_area():
     b=int(entrada_texto2.get())
     h=int(entrada_texto.get())
     p=(b*2)+(h*2)
     a=b*h
     etiqueta2.config(text="El area es {} y el perimetro es {}".format(a,p))
     
  


app.mainloop() 
