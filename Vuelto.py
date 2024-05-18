from tkinter import *
from tkinter import messagebox

interfaz=Tk()
interfaz.geometry("500x300+100+100")

def cambio():
    precioAux=precio.get()
    pagoAux=pago.get()
    cambioAux=pagoAux-precioAux
    faltanteAux=precioAux-pagoAux

    if(cambioAux<0):
        messagebox.showinfo(title="Ejercicio 2", message="Falta dinero en el pago: "+ str(faltanteAux))
    elif(cambioAux==0):
        messagebox.showinfo(title="Ejercicio 2", message="Se pago exacto: ")
    elif (cambioAux>0):
        messagebox.showinfo(title="Ejercicio 2", message="El cambio es: "+ str(cambioAux))


interfaz.title("Ejecicio2")
lblTitle=Label(text="***¿Cuanto cambio dar en una compra?***", font=("AR CENA",14)).pack()

lblIngrese=Label(text="Ingrese el precio del articulo: ", font=("Agency FB",14)).place(x=10,y=40)
precio=DoubleVar()
txtIngrese=Entry(interfaz,textvariable=precio).place(x=270,y=48)

lblPago=Label(text="¿Cuanto ha pagado el cliente?: ", font=("Agency FB",14)).place(x=10,y=70)
pago=DoubleVar()
txtPago=Entry(interfaz,textvariable=pago).place(x=270,y=78)

btnResultado=Button(interfaz,text="Calcular",command=cambio,font=("Agency FB",14)).place(x=10,y=110)

interfaz.mainloop()







#Construye un programa que al recibir como datos el costo de un articulo vendido y la cantidad de dinero entregada por el cliente calcule e imprima:
#1. El cambio q se debe de entregar al cliente, si el pago efectuado es mayor que el precio del producto
#2. ¿Qué pasa si el cliente pada exactamente lo que vale el producto
#3. La cantidad de dinero q falta por pagar, si el pago efectuado es menor que el precio del producto

"""precio=float(input("Ingrese el precio del articulo: "))
paga=float(input("Cuanto a pagado el cliente?:  "))

cambio=paga-precio
faltante=precio-paga

if (cambio<0):
    print("Falta dinero en el pago: ", faltante)
elif(cambio==0):
    print("Se a pagado exacto")
elif(cambio>0):
    print("el vuelto es: ", cambio)"""