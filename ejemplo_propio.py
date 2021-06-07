def run():

    print("Adivinanza sobre comida: Blanca por dentro, verde por fuera. Si no sabes, espera.\nTienes 5 intentos.")
    intentos = 0

    while intentos < 5:
        respuesta = input("¿Cual es la respuesta?  ")
        intentos += 1
        if respuesta == "pera":
            print("Has acertado. La respuesta es pera.")
            break
        if intentos == 5:
            print("Lo siento, se acabaron los intentos")


if __name__ == "__main__":
    run()