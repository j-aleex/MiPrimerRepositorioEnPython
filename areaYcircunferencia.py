from tkinter import *  
from tkinter import messagebox
import math

interfaz=Tk()
interfaz.geometry("500x300+100+100")
interfaz.title("Ejecicio circunferencia")
lblTitle=Label(text="***Area y Longitud de circunferencia ***", font=("AR CENA",14)).pack()

def longCal():
    longAux=radio.get()
    longRes=2*math.pi*longAux
    messagebox.showinfo(title="Ejercicio circulo", message="La longitud del circulo es: "+ str(longRes)) # type: ignore

def areaCal():
    areaAux=radio.get()
    areaRes=math.pi*pow(areaAux,2)
    messagebox.showinfo(title="Ejercicio circulo", message="El area del circulo es: "+ str(areaRes)) # type: ignore



lblRadio=Label(text="Ingrese el radio de la circunfencia: ", font=("Agency FB",14)).place(x=10,y=40)
radio=DoubleVar()
txtRadio=Entry(interfaz,textvariable=radio).place(x=270,y=48)

btnResultado=Button(interfaz,text="Calcular Longitud",command=longCal,font=("Agency FB",14)).place(x=10,y=110)
btnResultado=Button(interfaz,text="Calcular Area",command=areaCal,font=("Agency FB",14)).place(x=190,y=110)

interfaz.mainloop()












#Construye un programa q al recibir como dato el radio de un circulo, calcula e imprima tanto su area como la longitud de su circunferencia.

#1. El Area de un circulo la calculamos como:
#Area=pi * radio^2
#2. La circunferencia del circulo la calculamos de la siguiente forma:
#Longitud de la circunferencia = 2*pi*radio

"""import math

radio=float(input("Ingrese radio del circulo: "))

area=math.pi*pow(radio,2)
circunferencia=2*math.pi*radio

print("El area del circulo es: ", area)
print("La longitud del circulo es: ", circunferencia)"""
