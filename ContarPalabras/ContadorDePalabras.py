texto = "La ciudad fin de Buenos Aires. ciudad es conocida es conocida como la paris de America"
palabra = texto.split(" ")
print(palabra)
miNuevaLista =  list(set(palabra))

contPalabrasTotal = 0;
contPalabra = 0;
#Cuento el numero total de palabras que hay en el texto
print("El número total de palabras son: ",len(palabra))
print()
#Cuento cuantas veces se esta repitiendo la mima palabra en el texto
for i in range (0,len(miNuevaLista)):
    palabraTemp = miNuevaLista[i]
    for j in range (0,len(palabra)):
        if(palabra[j] == palabraTemp):
            contPalabra=contPalabra+1;
    print('"'+palabraTemp+'":',contPalabra)
    contPalabra=0;


