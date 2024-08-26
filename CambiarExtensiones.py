from pathlib import Path

#modificar la ruta en caso de testeos
carpeta = Path("c:/Python Project/Proyectos/CambiarExtensionesDeArchivos/CarpetaDeArchivos")

#iteramos para cada archivo dentro de la carpeta y si es .txt los cambiamos a .csv
for c in list(carpeta.iterdir()):
    if c.suffix == ".txt":
        nueva_extension = c.with_suffix(".csv")
        c.rename(nueva_extension)


#iteramos para cada subcarpeta dentro de la carpeta principal los archivo dentro, y, si son .csv los cambiamos a .txt
for c in carpeta.glob("**/*.csv"):
    nueva_extension = c.with_suffix(".txt")
    c.rename(nueva_extension)

#En este caso podemos modificar las extensiones segun los cambios que deseemos