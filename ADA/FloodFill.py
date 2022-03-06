from tkinter import *
from PIL import Image, ImageTk
from random import *
from time import time

ancho = 50
largo = ancho

#Crear la imagen
flood = Image.new("RGB", (ancho, largo), (0,0,0))
#flood = Image.open('flood1.png','r')

#Alterar la imagen
x = 0
y = 0
while x < ancho -1:
   y=0
   while y < largo -1:
       n = random()
       if n < .25:
          flood.putpixel((x,y), (0,0,0))
       else:
          flood.putpixel((x,y), (255,255,255))
       y+=1
   x+=1

def Floodfill(x, y, rojo, verde, azul, imagen, cont):
    cont+=1
    (r,g,b) = imagen.getpixel((x,y))
    if cont == 1000:
        return
    if (r,g,b) == (255,255,255):
        imagen.putpixel((x,y), (rojo,verde,azul)) #Colorear pixel
        Floodfill(x-1, y, rojo, verde, azul, imagen, cont)
        Floodfill(x+1, y, rojo, verde, azul, imagen, cont)
        Floodfill(x, y-1, rojo, verde, azul, imagen, cont)
        Floodfill(x, y+1, rojo, verde, azul, imagen, cont)
#Funcion para encontrar un pixel blanco
def Blanco(a, flood):
    (x,y)=(0,0)
    (r,g,b) = flood.getpixel((x,y))
    while (r,g,b) != (255,255,255):
        if x < a:
            (r,g,b) = flood.getpixel((x,y))
            x+=1
        else:
            y+=1
            x=0
    return x,y

(x,y) = Blanco(ancho, flood)
print(x)
print(y)
flood.save("flood1.png")
pantalla = Tk()
pantalla.title("Flood fill")
pantalla.geometry("650x500")
image = PhotoImage(file="flood1.png")
Label(pantalla, image=image).pack()
Label(pantalla, text="Imagen sin Flood fill").pack()
start_t = time()
Floodfill(x,y,255,0,0,flood, 0)
print("Tiempo de ejecucion: ", time() - start_t)
flood.save("flood2.png")
filledImg = PhotoImage(file="flood2.png")
Label(pantalla, image=filledImg).pack()
Label(pantalla, text="Imagen con Flood fill").pack()
pantalla.mainloop()