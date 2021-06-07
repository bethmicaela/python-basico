def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:  # Si contador al dividirlo por dos, el resto de la division es distinto de cero voy a saltarme esta vuelta del ciclo y lo que esta debajo de la palabra continue no se va a ejecutar.
    #         continue
    #     print(contador)
    
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break  # cortar / frenar 

    texto = input("Escribe un texto: ") # Pedir al usuario que ingrese un texto
    for letra in texto: 
        if letra == "o": # Si letra es igual a O, frenar.
            break
        print(letra)


if __name__ == "__main__":
    run()