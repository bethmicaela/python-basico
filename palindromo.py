def palindromo(palabra):
    palabra = palabra.replace(" ", "")   # quitamos los espacios, asi la computadora lo puede comprender, ej: Luz azul
    palabra = palabra.lower()   # convierto la palabra a letras en minuscula
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo  = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")
    

if __name__ == "__main__":    # punto de entrada de un programa de python, en este caso hacemos corrrer la funcion run()
    run()
