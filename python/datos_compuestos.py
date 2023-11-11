lista=["jesus","juan", "luis"]#lista pueden modificarse 
tupla=("jesus","juan", "luis")#las tuplas  no se puede modificar 
print(lista)

lista[2]="carlos" # cambia de un elemento ya asignado a uno nuevo 

print(lista )

#creando un conjunto set nose accede a elemntos por indice, no almacena datos duplicados 
conjunto={"Lucas Dalto","jesus", True,1.56}


#creando un diccionario (dict) (La estructura es key : value y separamos con comas  )

diccionario= {
    'nombre' : "jesus esquibel",
    'estado' : "Jalisco",
    'edad'   : "25 años",
    'trabajo': "flex"   
    }

print(diccionario['nombre'])