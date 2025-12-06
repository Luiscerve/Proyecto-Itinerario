# Ejemplo de manejo de archivos en Python
with open("ejemplo.txt", "w") as f:
    f.write("Este es un archivo de ejemplo.\n")

with open("ejemplo.txt", "r") as f:
    contenido = f.read()
    print("Contenido del archivo:", contenido)
