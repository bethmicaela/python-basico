   # contador = 0
   # print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

   # contador = 1
   # print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))



def run():
    LIMITE = 1000 # para definir una constante, lo colocamos todo en MAYUSCULA

    contador = 0 # variable que va a ir aumentando para multiplicar a 2 * 2, tantas veces como el contador lo diga
    potencia_2 = 2**contador # 2 elevado a contador
    while potencia_2 < LIMITE: # mientras potencia_2 sea menor a LIMITE: ejecuta lo que está debajo hasta que ya no se cumpla la condicion, terminando el ciclo.
        print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == "__main__":
    run()