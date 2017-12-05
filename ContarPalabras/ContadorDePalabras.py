#contador de palabras

def leertxt():
    print("")
    archi=open('textoPython.txt','r')
    lineas=archi.readline()
    print(lineas)
    palabra = lineas.split()
    miNuevaLista = list(set(palabra))
    contador=0

    contPalabrasTotal = 0;
    contPalabra = 0;

    print("")
    for p in range (0,len(palabra)):
        contador+=1

    # Cuento el numero total de palabras que hay en el texto
    print("El número total de palabras son: ", len(palabra))
    print()
    # Cuento cuantas veces se esta repitiendo la mima palabra en el texto
    for i in range(0, len(miNuevaLista)):
        palabraTemp = miNuevaLista[i]
        for j in range(0, len(palabra)):
            if (palabra[j] == palabraTemp):
                contPalabra = contPalabra + 1;
        print('"' + palabraTemp + '":', contPalabra)
        contPalabra = 0;

    print("##################### ARREGLO ######################\n")
    print(palabra)
    print("El total de palabras es: "+str(contador))
    archi.close()

leertxt()

