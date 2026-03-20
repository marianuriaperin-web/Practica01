import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

word = random.choice(words)
guessed = []
attempts = 6
points = 0

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
	    
    print(progress)

    # Verificar si ganó
    if "_" not in progress:
        points += 6
        print("¡Ganaste!")
        print (f"Puntaje: {points}")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")
    if len(letter) != 1 or not letter.isalpha():
        print ("Entrada no valida")
        print()
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        points -= 1
        print("Esa letra no está en la palabra.")
    
    print()

else:
    points = 0
    print(f"¡Perdiste! La palabra era: {word}")
    print (f"Puntaje: {points}")
    