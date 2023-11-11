# Creamos una lista con list()
lista = list(["hola","jesus",34,56,52,True])

#devuelve la cantidad de elementos de la lista 
cantidad_elementos = len(lista)

#agregando un elemento a la listo 
lista.append("JAJAJA")

#agregando un elemento a la lista en un indice especifico
lista.extend(2,"Toma juan")

#agregando varios elementos a la lista 
lista.extend([False,2030])

#eliminando un elemento de la lista (por su indice)
lista.pop(3) #-1 para eliminar el ultimo elemento, -2 para eliminar el anteultimo y asi sucesivamente

#removiendo un elemento de la lista por su valor 
lista.remove("Toma juan")

#eliminando todos los elemntos de la lista 
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=true lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista 
lista.reverse()



