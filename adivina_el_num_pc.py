import random


def adivina_el_numero_pc(x):
    print("---------------------")
    print("    ¡Bienvenidxs!    ")
    print("---------------------")
    print(f"Selecciona un número entre 1 y {x} para que la computadora lo adivine: ")

    limite_inferior=1
    limite_superior=x
    respuesta=""

    while respuesta != "c":
        if limite_inferior!=limite_superior:
            predict=random.randint(limite_inferior,limite_superior)
        else:
            predict=limite_inferior
        respuesta=input(f"La predicción de la computadora es: {predict}.\nSi es muy grande, ingresa (A).\nSi es muy pequeña, ingresa (B).\nSi es correcta, ingresa (C).\n").lower()
        if respuesta=="a":
            limite_superior=predict-1
        elif respuesta=="b":
            limite_inferior=predict+1
    print(f"¡Fantástico! La computadora adivinó que el número seleccionado es {predict}.")


adivina_el_numero_pc(10)