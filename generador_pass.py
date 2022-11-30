import random
import string


abecedario=string.ascii_letters
numeros=string.digits
simbolos=string.punctuation
caracteres=abecedario+numeros+simbolos


def generadorPass():
    password=""
    cantidad_caract=input("¿De cuántos caracteres?:")
    while cantidad_caract.isnumeric()==False:
        print("Debes ingresar un número entero.")
        cantidad_caract=input("¿De cuántos caracteres?:")
    if cantidad_caract in simbolos:
        print("Debes ingresar un número entero.")
        cantidad_caract=input("¿De cuántos caracteres?:")
    else:
        for index in range(int(cantidad_caract)):
            password=password+random.choice(caracteres)
        print(f"Tu contraseña generada es: '{password}'")


generadorPass()