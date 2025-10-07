#ahorcado
import random

palabras = [
    "casa", "perro", "gato", "arbol", "cielo",
    "fuego", "agua", "tierra", "sol", "luna",
    "estrella", "rio", "mar", "bosque", "flor",
    "hoja", "piedra", "montana", "valle", "nube",
    "viento", "arena", "camino", "puente", "ciudad",
    "escuela", "carro", "libro", "mesa", "silla",
    "puerta", "ventana", "pared", "campo", "pueblo",
    "barco", "avion", "tren", "camion", "reloj"
]

eleccion_ia = random.choice(palabras)
intentos = 30
palabra = "_" * len(eleccion_ia)
lista = list(palabra) 
letras = ""

while True:
    eleccion_usu = input("Ingrese una letra: ")
    intentos -= 1
    letras = letras + eleccion_usu

    print("Letras incorrectas:")
    for letra in set(letras):
        if letra not in eleccion_ia:
            print(letra, end="")
    print()

    if intentos == 0:
        print(f"Perdiste, la palabra era {eleccion_ia.upper()}")
        break

    if len(eleccion_usu) > 1:
        print("Solo puede ingresar un caracter")

    elif len(eleccion_usu) < 1:
        print("Debes ingresar un caracter")

    for i in range(len(eleccion_ia)):
        if eleccion_ia[i] == eleccion_usu:
            lista[i] = eleccion_usu

    palabra = "".join(lista)
    print(palabra.upper())
    
    if palabra == eleccion_ia:
        print(f"Ganaste, la palabra era {eleccion_ia.upper()}")
        break

    print(f"intentos restantes = {intentos}")   




