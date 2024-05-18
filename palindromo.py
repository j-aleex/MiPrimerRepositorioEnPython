cadena=input("Ingresa la palabra: ")

def esPalindromo(cadena):
    cadena=cadena.lower()  #Vuelve minusculas
    cadena=cadena.replace(" ","")#reemplaza caracteres
    cadena=cadena.replace("á","a")
    cadena=cadena.replace("é","e")
    cadena=cadena.replace("í","i")
    cadena=cadena.replace("ó","o")
    cadena=cadena.replace("ú","u")
    if str(cadena)==str(cadena)[::-1]:
        return True
    else:
        return False

if esPalindromo(cadena):
    print("Es palindromo")
else:
    print("No es palindromo")
    


"""Solucion 1
if str(cadena)==str(cadena)[::-1]:
    print("Es palindromo")
else:
    print("No es palindromo")"""


"""soucion 2
def esPalindromo(cadena):
    cadena=cadena.lower()  #Vuelve minusculas
    cadena=cadena.replace(" ","")#reemplaza caracteres
    cadena=cadena.replace("á","a")
    cadena=cadena.replace("é","e")
    cadena=cadena.replace("í","i")
    cadena=cadena.replace("ó","o")
    cadena=cadena.replace("ú","u")
    
    a=0 #inicio 
    b=len(cadena)-1   #El largo de la cadena, tamaño, ultima letra
    for i in range(0, len(cadena)):
        if cadena[a]==cadena[b]:
            a+=1
            b-=1
        else:
            return False
    return True

if esPalindromo(cadena):
    print("Es palindromo") 
else:
    print("No es palindromo")"""