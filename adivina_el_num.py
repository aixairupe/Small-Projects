import random


def adivina_el_numero(x):
    print("---------------------")
    print("    ¡Bienvenidxs!    ")
    print("---------------------")
    print("La meta del juego es adivinar el número")
    print("¡Vamos allá!")
    
    random_num=random.randint(1,x)
    predict=0

    while predict!=random_num:
        predict=int(input(f"Adivina el número entre 1 y {x}: "))
        if predict<random_num:
            print("El número elegido es muy pequeño, intenta otra vez.")
        elif predict>random_num:
            print("El número elegido es muy grande, intenta otra vez.")
    print(f"¡Genial! Adivinaste, el número {predict} es correcto.")


adivina_el_numero(5)