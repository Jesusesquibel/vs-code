#le pedimos al usuario que nos diga una frace
frase = input("escribe una frace y calculo cuato tardarias si tuvieras que decierla")

#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos  len() para ver la cantidad de elementos que hay en la lsita 
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco
if  cantidad_de_palabras > 10:
    print("para no te pedimos un libro")
    
#Calculemos cuanto tardaria en decir las palabras y se lo decimos 

print(f'Dijiste{cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Jesus lo diria en {cantidad_de_palabras * 100// 2*1.3 / 100} segundos')