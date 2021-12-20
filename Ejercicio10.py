#Repita la lectura de un número entero hasta que sea positivo, entonces, 
# determine cuantas cifras tiene. El método que debe usar es contar cuantas veces es divisible para 10.
import sys
from tkinter import *

def operar():
    conta=1
    j=10
    x=int(entry1.get())
    if(x>=0):
        while j <= x:
            conta = conta +1
            j = j * 10
        etiqueta2.config(text="el numero "+str(x)+", esta comppuesto de: "+str(conta)+" cifras")
    else:
        etiqueta2.config(text="ingrese un numero positivo")


app=Tk()
app.title=("DIVISIBLE")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(100,100))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiquetan=Label(app, text=("Cifras de un numero positivo"))
etiquetan.grid(column=0, row=0)
etiqueta=Label(app, text=("Ingrese un numeo positivo"))
etiqueta.grid(column=0, row=1)
etiqueta2=Label(app, text=("Respuesta"))
etiqueta2.grid(column=0, row=6)

entry1=Entry(app)
entry1.grid(column=0, row=4) 

boton=Button(app, text="determinar cifras", command=operar)
boton.grid(column=0, row=5)

app.mainloop()