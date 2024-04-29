from Speech import speech
import random
import time

niveles = {
    "facil": ["agenda", "ami", "souris"],
    "intermedio": ["ordinateur", "algorithme", "développeur"],
    "dificil": ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"],
}

def play_game(nivel):
    palabras = niveles.get(nivel, [])
    if not palabras:
        print("Nivel de dificultad incorrecto")
        return
    puntos = 0
    intentos = 3

    for i in range(len(palabras)):
        palabra = random.choice(palabras)
        
        try: 
            for j in range(intentos):
                print(f'Por favor pronunciar la siguiente palabra {palabra}')
                reco_palabra = speech()
                print(reco_palabra)

                if palabra == reco_palabra:
                    print("Correcto")
                    puntos += 1
                    break
                else:
                    print(f'Incorrecto la palabra es {palabra}')

        except:
            print("No entiendo lo que dices")

        
        time.sleep(2)
    
    print(f'¡se acabo el juego!, tu puntaje es: {(puntos/(len(palabras)))}')

nivel = input("Ingresa el nivel de dificultad (facil, intermedio o dificil): ").lower()
play_game(nivel)