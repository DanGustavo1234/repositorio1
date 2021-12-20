# Un bote tiene capacidad de llevar X kilos. 
# Se tiene una lista con los pesos en kilos ordenados en forma creciente 
# de las personas que desean subir al bote. Determine cuantas personas puede llevar el bote.
import sys
from tkinter import * 
import random

app = Tk()
app.title("Bote")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)
#Capacidad de carga 
valor=''
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=0, row=1) 
#Numero de personas en la lista 
valor1=''
entrada_texto1= Entry(vp, width=10, textvariable=valor1)
entrada_texto1.grid(column=2, row=1) 
#enviar
boton = Button(vp, text="enviar",command=lambda:calcula())
boton.grid(column=1, row=2)
#etiqueta capacidad de carga
etiqueta= Label(vp,text="Capacidad de carga")
etiqueta.grid(column=0, row=0, sticky=(W,E)) 
#etiqueta numero de personas 
etiqueta1= Label(vp,text="Numero de personas")
etiqueta1.grid(column=2, row=0, sticky=(W,E)) 
#etiqueta respuesta 
etiqueta2= Label(vp)
etiqueta2.grid(column=1, row=4, sticky=(W,E)) 
#etiqueta respuesta 
etiqueta3= Label(vp)
etiqueta3.grid(column=1, row=5, sticky=(W,E)) 

def calcula():
     cont=0
     suma=0
     x=int(entrada_texto.get())
     y=int(entrada_texto1.get())
     lista_pesos=[]
     for i in range(1,y+1):
         lista_pesos.append(random.randint(30,150))
         lista_pesos.sort()
         etiqueta2.config(text="Lista de pesos {}".format(lista_pesos))
     
     for t in lista_pesos:
         suma=suma+t
         if suma<=x:
              cont+=1
         else:
             break
     etiqueta3.config(text="El bote puede llevar {} personas ".format(cont))

      





 




app.mainloop() 
