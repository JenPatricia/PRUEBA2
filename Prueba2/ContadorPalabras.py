# CÓDIGO PARA CONTAR PALABRAS

#Función para leer el texto del archivo y mostrarlo en pantalla

def leertxt():
    print("")
    archivo = open('textoPython.txt', 'r')
    lineasTexto = archivo.readline()
    print(lineasTexto)
    archivo.close()
    return lineasTexto

#Función para contar palabras del texto primera forma

def contarPalabras1():
    print('1. P R I M E R A   F O R M A   D E   C O N T A R   P A L A B R A S\n ' + '   \nC O N T E N I D O    D E L    A R C H I V O    TXT')
    leertxt()
    print()
    contar = 0
    archivo = open('textoPython.txt', 'r')
    for renglon in archivo:
        for palabra in renglon.split():
            contar += 1
            print ((str(contar) + ')' + ' ' + palabra))
    archivo.close()
    print ('\nEl texto tiene en total ' + str(contar) + ' palabras.\n')

#Función para contar palabras del texto segunda forma

def contarPalabras2():
    print('\n\n2. S E G U N D A   F O R M A   D E   C O N T A R   P A L A B R A S\n' + '    \nC O N T E N I D O    D E L    A R C H I V O    TXT')
    lineas = leertxt()
    palabra = lineas.split()
    miNuevaLista = list(set(palabra))
    contador = 0
    contPalabra = 0;
    print()

#Cuento el número total de palabras que hay en el texto por medio de la la lista

    print("El número total de palabras son: ", len(palabra), "\n")
    print()


# Cuento el número total de palabras que hay en el texto usando un contador
    print('\n3. T E R C E R A   F O R M A   D E   C O N T A R   P A L A B R A S\n')
    for p in range(0, len(palabra)):
        contador += 1
    print("C O N T E N I D O   D E   L A   L I S T A\n")
    print(palabra)
    print("\nEl total de palabras es: " + str(contador) + '\n')

# Cuento cuantas veces se esta repitiendo la misma palabra en el texto

    print("\n\nP A L A B R A S   Q U E   S E   R E P I T E N   E N   E L   T E X T O\n")
    for i in range(0, len(miNuevaLista)):
        palabraTemp = miNuevaLista[i]
        for j in range(0, len(palabra)):
            if (palabra[j] == palabraTemp):
                contPalabra = contPalabra + 1;
        print('(' + palabraTemp + ') se repite ' + str(contPalabra) + ' veces.\n')
        contPalabra = 0;

#Llamado a las funciones

contarPalabras1()
contarPalabras2()