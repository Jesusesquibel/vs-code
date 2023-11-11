cadena1 = "hola soy jesus"
cadena2 = "welcom to Jalisco"

#convierte a mayusculas 
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#primera letra en mayuscula
primer_letra_mayus = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay considencia devuelve -1
busqueda_find = cadena1.find("b")

#busqueda una cadena en otra cadena, si no hay concidencias lansa una ecepcion
busqueda_index = cadena1.index("H")

#si es numerico, devolvemos true, si no devolvemos false 
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true, si devolvemos false 
es_alfanumerico = cadena1.isalpha()

#contamos coincidencias de una cadena dentro de otra cadena, devolvemos la cantidad de coincidencias
contar_coincidencias = cadena1.coun("la ma")

#contamos cuantos caracteres tiene una cadena 
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true 
empieza_con = cadena1.startswith("H")

#remplza en pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("hola","jolalad")

#separar cadenas con la cadena que le pasamos 
cadena_separada = cadena1.split(",")

print(empieza_con)