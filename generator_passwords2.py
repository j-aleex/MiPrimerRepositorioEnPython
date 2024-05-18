import string
import random
from werkzeug.security import generate_password_hash

#Establecemos el tamaño 
longitud=int(input("Ingrese tamaño de la contraseña: "))

caracteres=string.ascii_letters+string.digits+string.punctuation

contraseña="".join(random.choice(caracteres) for i in range(longitud))#for para el tamaño
contraseña_encriptado=generate_password_hash(contraseña)
print("La contraseña generada es: {} => {}".format(contraseña,contraseña_encriptado))
