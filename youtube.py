from tkinter import *
from tkinter import messagebox as mb 
from PIL import Image, ImageTk
import os
import subprocess

# Ruta al ejecutable de yt-dlp
yt_dlp_path = os.path.join(os.getcwd(), 'bin', 'yt-dlp.exe')

def descargar_video():
    enlace = videos.get()
    ydl_opts = [
        yt_dlp_path,
        '-f', 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        '-o', os.path.join('Videos', '%(title)s.%(ext)s'),
        enlace
    ]
    
    # Ejecutar yt-dlp con subprocess
    try:
        subprocess.run(ydl_opts, check=True)
        mb.showinfo('Éxito', 'El video se descargó correctamente.')
    except subprocess.CalledProcessError as e:
        mb.showerror('Error', f'Hubo un problema al descargar el video: {e}')
    except Exception as e:
        mb.showerror('Error', f'Ocurrió un error inesperado: {e}')

def descargar_audio():
    enlace = videos.get()
    ydl_opts = [
        yt_dlp_path,
        '-f', 'bestaudio/best',
        '-o', os.path.join('Música', '%(title)s.%(ext)s'),
        '--postprocessor-args', '-codec:a libmp3lame -qscale:a 2',
        enlace
    ]
    
    # Ejecutar yt-dlp con subprocess
    try:
        subprocess.run(ydl_opts, check=True)
        mb.showinfo('Éxito', 'El audio se descargó correctamente.')
    except subprocess.CalledProcessError as e:
        mb.showerror('Error', f'Hubo un problema al descargar el audio: {e}')
    except Exception as e:
        mb.showerror('Error', f'Ocurrió un error inesperado: {e}')

root = Tk()
root.config(bd=15)
root.title('Descargar videos de YouTube')

# Configuración de imagen
imagen_original = Image.open('youtube_black.png')
ancho_maximo = 200
ratio = ancho_maximo / imagen_original.width
altura = int(imagen_original.height * ratio)
imagen_redimensionada = imagen_original.resize((ancho_maximo, altura))

imagen = ImageTk.PhotoImage(imagen_redimensionada)
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)

menubar.add_command(label='Ayuda', command=lambda: mb.showinfo('Ayuda', 'Ingrese la URL del video y elija si desea descargar el video o solo el audio.'))
menubar.add_cascade(label='Salir', command=root.destroy)

def on_entry_click(event):
    if videos.get() == 'Ingrese el link del video':
        videos.delete(0, "end")  # borra todo el contenido de la caja de texto
        videos.insert(0, '')  # inserta una cadena vacía
        videos.config(fg='black')

def on_focusout(event):
    if videos.get() == '':
        videos.insert(0, 'Ingrese el link del video')
        videos.config(fg='grey')

instrucciones = Label(root, text='Programa creado en Python \n', font=('Arial', 12))
instrucciones.grid(row=0, column=1)

videos = Entry(root, width=50, fg='grey')
videos.insert(0, 'Ingrese el link del video')
videos.bind('<FocusIn>', on_entry_click)
videos.bind('<FocusOut>', on_focusout)
videos.grid(row=1, column=1)

boton_video = Button(root, text='Descargar Video 🎬', command=descargar_video, width=20, height=2, bg='red', fg='white')
boton_video.grid(row=2, column=1)

boton_audio = Button(root, text='Descargar Audio 🎵', command=descargar_audio, width=20, height=2, bg='blue', fg='white')
boton_audio.grid(row=3, column=1)

root.mainloop()