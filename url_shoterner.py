import pyshorteners  #Libreria para el proceso de cortar url
import streamlit as st #Libreria para crear pagina web

def shorten_url(url): #Funcion que recibe la url
    s = pyshorteners.Shortener()  #Crear objeto 
    shortened_url = s.tinyurl.short(url) #Llamar metodo para cortar url
    return shortened_url #devolver la url recortada



#creamos app web con stremamlit
st.set_page_config(page_title="URL Shortener", page_icon="✏️", layout="centered")
#1. Configuramos la pagina ( titulo, icono, layout centrado(Pagiana web))
#st.image("images/www.png", use_column_width=True) #añadir imagen 
st.title("URL Shortener")  #titulo
url = st.text_input("Enter the URL") #insertar url q se desea acortar


if st.button("Generate new URL"): #Boton para recortar url 
    st.write("URL shortened: ", shorten_url(url)) #Mostrar nueva url


#Ejecutar
#streamlit run url_shoterner.py