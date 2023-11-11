#para encontrar numeros pares o inpares de una lista 

numero = [ 1,23,4,5,6,78,92,90,53,423,223,1132]

#multiplicador_por_dos = lambda x : x*2

#def es_par(num):
#    if(num%2==0):
#        return True
    
#numeros_pares = filter(es_par,numero)    
    
#print(list(numeros_pares))

# Lo mismo que lo anterior pero con funcion lambda

numeros_pares = filter(lambda numero:numero%2==0,numero)
print(list(numeros_pares))