## Actualizar yt-dlp.exe

Para asegurarte de tener la última versión de `yt-dlp.exe`, puedes ejecutar el siguiente comando en PowerShell dentro de la carpeta del proyecto:

```powershell
Invoke-WebRequest -Uri "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe" -OutFile "bin\yt-dlp.exe"
```

# Proyecto_Convertidor

Proyecto implementado en Python que utiliza yt-dlp y ffmpeg para descargar videos o audios de YouTube a partir de una URL.


## Requisitos

- Python 3.x
- Pillow (`pip install pillow`)

Dentro de la carpeta `bin` se encuentran los archivos `yt-dlp.exe` y `ffmpeg.exe`, por lo que no es necesario instalarlos manualmente.

## Uso

1. Ejecuta el script `youtube.py`.
2. Ingresa la URL del video de YouTube.
3. Haz clic en "Descargar Video" para obtener el video o en "Descargar Audio" para obtener solo el audio en MP3.


## Notas

- Si tienes problemas para descargar, asegúrate de tener la última versión de `yt-dlp.exe` en la carpeta `bin`.


![image](https://github.com/user-attachments/assets/150ed253-233d-4a39-8a6d-9f23addf83ae)

**Nota:** Para poder acceder al ejecutable se tiene que acceder a la carpeta dist -> youtube_downloader y dar doble clic a youtube_downloader.exe

![Imagen2](https://github.com/user-attachments/assets/9297c617-2e35-4028-931f-2a2c915480dd)
