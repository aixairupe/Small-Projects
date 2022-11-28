import random
import string


AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']


palabras = ["aire", "ojos", "piel", "anteojos", "joven", "viejo", "alto", "bajo", "pequeño", "gordo", "delgado", "bella", "azul", "verde", "negro", "sombrero", "guantes", "corbata", "gemelos", "paraguas", "plata", "oro", "perla", "diamante", "esmeralda", "anillo", "pulsera", "reloj", "elegante", "sencillo", "chaqueta", "traje", "camisa", "zapatos", "pelo", "maquillaje", "peine", "dedo", "hueso", "cara", "ojo", "calor", "ambulancia", "enfermera", "farmacia", "vitaminas", "pastillas", "dentista", "ciego", "correr", "caminar", "regresar", "saltar", "fin", "cerrar", "nombre", "mujer", "hombre", "soltero", "novio", "nacer", "vivir", "edad", "anciana","trabajar", "cobrar", "azafata", "artista", "panadero", "carpintero", "cocinero", "maestro", "bombero", "juez", "modelo", "monje", "pintor", "piloto", "secretaria", "taxista", "escritor", "jefe", "aprendiz", "jubilado", "empleo", "industria", "taller", "tienda", "vacaciones", "sueldo", "impuesto", "huelga", "obedecer", "locura", "humor", "inteligencia", "orgullo", "timidez", "valiente", "aburrido", "loco", "divertido", "bueno", "feliz", "amable", "pobre", "serio", "extraño", "gritar", "llorar", "suspirar", "preocupado", "risa", "amor", "suerte", "enamorado", "ver", "apagar", "luz", "color", "lupa", "microscopio", "claro", "cantar", "silbar", "voz", "eco", "trueno", "altavoz", "radio", "auricular", "liso", "comer", "dulce", "salado", "perfume", "despertarse", "vestirse", "desayunar", "leer", "dormirse", "toalla", "cobija", "almuerzo", "sopa", "agua", "leche", "jugo", "sal", "pimienta", "vinagre", "ajo", "perejil", "menta", "canela", "mayonesa", "pan", "mantequilla", "miel", "manzana", "pera", "durazno", "cereza", "papa", "lechuga", "arroz", "pollo", "pavo", "hamburguesa", "camarones", "tortilla", "espagueti", "sopa", "helado", "chocolate", "galletas", "bombones", "limpiar", "cortar", "hervir", "planchar", "aspiradora", "plancha", "horno", "abrelatas", "vajilla", "vaso", "cafetera", "azucarera", "comprar", "gastar", "vender", "barato", "caro", "gratis", "cliente", "bolsa", "precio", "recibo", "ascensor", "esquiar", "ciclismo", "golf", "pelota", "tenis", "bicicleta", "estadio", "gol", "torneo", "leer", "dibujar", "cantar", "bailar", "libro", "revista", "clavo", "cine", "pala", "cocina", "hielo", "coro", "piano", "cartas", "pesca", "radio", "noticias", "televisor", "documental", "anuncio", "aplaudir", "teatro", "circo", "mago", "disco", "portero", "propina", "regalo", "fiesta", "vela", "alfombra", "puerta", "ventana", "cortina", "escritorio", "cuadro", "juguete", "alquiler", "mudanza", "casa", "pared", "chimenea", "comedor", "plaza", "calle", "estacionamiento", "parque", "puente", "puerto", "edificio", "escuela", "museo", "estatua", "fuente", "turista", "mendigo", "manejar", "acelerar", "frenar", "cruzar", "reparar", "conductor", "multa", "atasco", "carretera", "peaje", "curva", "florecer", "campo", "bosque", "huerto", "selva", "tronco", "rama", "flor", "hoja", "musgo", "cedro", "roble", "pino", "nogal", "naranjo", "tallo", "clavel", "margarita", "amapola", "rosa", "girasol", "violeta", "gato", "perro", "vaca", "pato", "oveja", "conejo", "pez", "oso", "jirafa", "erizo", "mariposa", "foca", "tigre", "cobra", "almeja", "paloma", "cisne", "mosquito", "hormiga", "llover", "nevar", "nublado", "soleado", "clima", "rayo", "nieve", "sol", "viento", "padre", "madre", "hijo", "abuela", "estudioso", "aula", "tiza", "regla", "computadora", "diccionario"]



def selecPalabra(palabras):
  palabra=random.choice(palabras)
  return palabra.upper()

def buclePrincipal():
  letras_correctas=set()
  letras_incorrectas=set()
  letras_usadas=set()
  abecedario=set(string.ascii_uppercase)

  palabra_secreta=selecPalabra(palabras)
  
  vidas=7

  while vidas!=0:
    palabra=[letra if letra in letras_correctas else '_' for letra in palabra_secreta]
    print(f"La palabra por adivinar es: {palabra}")
    print(AHORCADO[len(letras_incorrectas)])    

    if vidas>1:
      print(f"Te quedan {vidas} vidas. Has usado las letras: {' '.join(letras_usadas)}")
    elif vidas==1:
      print(f"Te queda 1 vida. Has usado las letras: {' '.join(letras_usadas)}")
      
    letra_elegida=input("Ingrese una letra: ").upper()

    if letra_elegida in abecedario - letras_usadas:
      if letra_elegida in set(palabra_secreta):
        letras_usadas.add(letra_elegida)
        letras_correctas.add(letra_elegida)
        print("¡Adivinaste una letra!")
      else:
        letras_usadas.add(letra_elegida)
        letras_incorrectas.add(letra_elegida)
        vidas-=1
        print("Letra incorrecta.")
    elif letra_elegida in letras_usadas:
      print("La letra ya fue ingresada antes. Por favor, ingresa una nueva: ")
    else:
      print("El caracter no es una letra válida. Por favor, ingresa otro: ")
  if set(palabra_secreta)-letras_correctas==0:
    print(f"¡Felicitaciones! Has adivinado la palabra {palabra_secreta} correctamente.")
  else:
    print(f"¡Has perdido! La palabra era: {palabra_secreta}.")

buclePrincipal()