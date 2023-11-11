# Falto el profe y los alumnos va a armar un problema 

#funcion para obtener asistente y al profesor segun la edad 
def obtener_compañeros(cantidad_de_compañeros):
    
    #Creando la lista de compañeros 
    compañeros = []
    
    #ejecuta un for para pedir informacion de los compañeros
    for i in range (cantidad_de_compañeros):
        nombre = input("Nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        
        #Agrega la informacion a la lista 
        compañeros.append(compañero) 
        
    #ordena de menor a mayor segun la edad
    compañeros.sort(key=lambda x:x[1])  
    #Compañeors[x] devuelve uns tupla (nombre, edad) y despues accedemos al nombre 
    #para defenir al asistente y al profesor 
    asistente = compañeros [0][0]
    profesor  = compañeros [-1][0] 
    
    #retornamos una tupla
    return asistente, profesor
#se desempaqueta lo que esta devolviendo la funcion 
asistente, profesor = obtener_compañeros(3) 

#mostrar el resultado 
print(f"El profesor es: {profesor} y su asistente es {asistente} ")