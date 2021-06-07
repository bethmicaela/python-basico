def es_primo(numero): # numero que ingresa el usuario
    contador = 0 

    for i in range(1, numero + 1): # numero 1 para que aparezca el 1 hasta el número que ingresó el usuario y que no se corte uno antes.
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input("Escribe un numero: "))
    if es_primo(numero): # Se puede obviar el == True:
        print("Es primo")
    else:
        print("No es primo")



if __name__ == "__main__":
    run()