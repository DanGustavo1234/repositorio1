#Escriba un programa que pida el año actual y un año cualquiera y que
#escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.
import sys
from tkinter import * 
app = Tk()
app.title("Años")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(100,100), pady=(100,100))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

boton2 = Button(vp, text="enviar",command=lambda:años())
boton2.grid(column=2, row=2)

valor=''
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=1, row=1)

valor1=''
entrada_texto1 = Entry(vp, width=10, textvariable=valor1)
entrada_texto1.grid(column=3, row=1)

etiqueta= Label(vp,text="Año actual")
etiqueta.grid(column=0, row=1, sticky=(W,E))       

etiqueta1 = Label(vp,text="Año cualquiera")
etiqueta1.grid(column=2, row=1, sticky=(W,E))

etiqueta2 = Label(vp)
etiqueta2.grid(column=11, row=3, sticky=(W,E))



def años():
     año_actual=int(entrada_texto1.get())
     año_cualquiera=int(entrada_texto.get())
     if año_actual<=año_cualquiera:
         x=año_cualquiera-año_actual
         etiqueta2.config(text=" Han pasado {} años".format(x))
     else:
         x=año_actual-año_cualquiera
         etiqueta2.config(text=" Faltan {} años".format(x))
app.mainloop() 



