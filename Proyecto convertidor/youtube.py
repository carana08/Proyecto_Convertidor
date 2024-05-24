from pytube import YouTube
from tkinter import *
from tkinter import messagebox as mb 
from PIL import Image, ImageTk


def accion():
    enlace=videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()


root = Tk()
root.config(bd=15)
root.title('Descargar videos de YouTube')

imagen_original = Image.open('youtube_black.png')
ancho_maximo = 300 
ratio = ancho_maximo / imagen_original.width
altura = int(imagen_original.height * ratio)
imagen_redimensionada = imagen_original.resize((ancho_maximo, altura))


imagen = ImageTk.PhotoImage(imagen_redimensionada)
foto = Label(root,image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0) 

menubar.add_command(label='Ayuda', command=lambda: mb.showinfo('Ayuda', 'Para descargar un video de YouTube, ingrese la URL del video en el campo de texto y haga clic en el botón Descargar.'))
menubar.add_cascade(label='Salir', command=root.destroy)

instrucciones = Label(root, text='Programa creado en Python con Ayuda de Youtube\n', font=('Arial', 12))
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text='Descargar 😊', command=accion)
boton.grid(row=2, column=1)

root.mainloop()


