def contraseña_random(num):
    chars = "oiahisaoh"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5 
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

#desempaquetando la funcion 
password,primer_numero = contraseña_random(981)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlos
print(f"tu contraseña nueva es:{password} ")
print(f"El numero utilizado para crearla fue{primer_numero}")