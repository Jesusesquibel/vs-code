#se crea una lista
animales = ["camaro,","pez","gato","cocdrilo","raton","iguana"]

#creando bucle for 
for animal in animales:
    print(f'ahora la variable animal es igual a : {animal}')
#---------------------------------------------------------------

#creando recorrido de numeros
numeros = [2,2,3,5,6,7,8,9]
for numero in numeros:
    resultado = numero *100 # al recorrido del ciclo for se va a multiplicar por x cantidad 
    print(resultado)   
    
    
#para iterar dos listas al mismo tiempo, realizando el mismo recorrido en las dos listas a la vez, pero las listas tienen que tener la misma cantidad de elementos
for numeros,animales in zip(numeros,animales):
    print(f"recorrido a lista 1 : {numeros}")
    print(f"recorrido a lista 2 : {animales}")
 
 
 #forma inciorrecta de recorrer una lista    
for num in range(len(numeros)):
    print(numeros[num])
    
    
#forma correcta de recorrer una lista con su indice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print (f'el indcie es :{indice} y el valir es :{valor}')
    
    
    
#usando el for/else 
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actural: {numero}')
else:
    print("el bucle termino")
    
# TODO LO ANTERIOR FUNCIONA EXACTAMENTE IGUAL PARA TUPLAS 
    
    
