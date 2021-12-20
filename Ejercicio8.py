#Un comerciante compra un artículo a un costo dado. Determine el precio al cual debe venderlo si desea ganar el 15%.
import sys
from tkinter import * 
import random

app = Tk()
app.title("Ganancia 15%")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

boton = Button(vp, text="enviar",command=lambda:calcula())
boton.grid(column=0, row=2)

valor=''
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=0, row=1) 

etiqueta= Label(vp,text="Ingrese el monto del comerciante")
etiqueta.grid(column=0, row=0, sticky=(W,E)) 

etiqueta1= Label(vp)
etiqueta1.grid(column=0, row=3, sticky=(W,E)) 

def calcula():
    x=int(entrada_texto.get())
    ganancia=(x*0.15)+x
    etiqueta1.config(text="El precio de venta es {}".format(ganancia))
app.mainloop() 
