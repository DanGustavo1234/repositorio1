# Escriba un programa que pregunte primero si
# se quiere calcular el área de un triángulo
# o la de un círculo. Si se contesta que se
# quiere calcular el área de un triángulo (boton),
# el programa tiene que pedir entonces la base y 
# la altura y escribir el área. Si se contesta que se quiere
# calcular el área de un círculo (boton), el programa tiene
# que pedir entonces el radio y escribir el área. Se recuerda 
# que el área de un triángulo es base por altura dividido por 2
# y que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.
import sys
from tkinter import * 
import math


app = Tk()
app.title("Años Bisiestos")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(60,60), pady=(60,60))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

#Triangulo
boton2 = Button(vp, text="enviar",command=lambda:area_triangulo())
boton2.grid(column=1, row=2)

valor1=''
entrada_texto1 = Entry(vp, width=10, textvariable=valor1)
entrada_texto1.grid(column=1, row=1)

valor=''
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=3, row=1)

etiqueta1= Label(vp,text="Base")
etiqueta1.grid(column=0, row=1, sticky=(W,E))   

etiqueta2= Label(vp,text="Altura")
etiqueta2.grid(column=2, row=1, sticky=(W,E))   

etiqueta= Label(vp,text="Area de un triangulo")
etiqueta.grid(column=1, row=0, sticky=(W,E))   

etiqueta4= Label(vp)
etiqueta4.grid(column=4, row=1, sticky=(W,E))  
#Circulo
boton3 = Button(vp, text="enviar",command=lambda:area_circulo())
boton3.grid(column=1, row=5)

valor2=''
entrada_texto2 = Entry(vp, width=10, textvariable=valor2)
entrada_texto2.grid(column=1, row=4)

etiqueta3= Label(vp,text="Radio")
etiqueta3.grid(column=0, row=4, sticky=(W,E))   

etiqueta4= Label(vp,text="Area de un circulo")
etiqueta4.grid(column=1, row=3, sticky=(W,E))  

etiqueta6= Label(vp)
etiqueta6.grid(column=1, row=6, sticky=(W,E)) 

def area_triangulo():
     b=int(entrada_texto.get())
     h=int(entrada_texto1.get())
     areaT=(b*h)/2
     etiqueta4.config(text=("El area del triangulo es {}".format(areaT)))


def area_circulo():
     r=int(entrada_texto2.get())
     areaC=(math.pi)*r*r
     etiqueta6.config(text=("El area del circulo es {}".format(areaC)))
       

app.mainloop() 