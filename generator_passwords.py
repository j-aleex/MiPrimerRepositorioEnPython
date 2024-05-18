import random
from werkzeug.security import generate_password_hash

minus="abcdefghijklmnopqrstuvwxyz"
mayus=minus.upper()
numeros="0123456789"
simbolos="#$%&'()*+,-./:;<=>?@"


base=minus+mayus+numeros+simbolos
long=12

#for _ in range(100):  #Imprimit 100 claves
for _ in range(3):
    muestra=random.sample(base, long)
    #join para concatenar caracteres
    password="".join(muestra)
    password_encriptado=generate_password_hash(password)
    print("{} => {}".format(password, password_encriptado))


