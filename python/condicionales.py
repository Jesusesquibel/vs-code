contraseña_almacenada="Jalisco"
contraseña1_escrita="Jalisco"
if contraseña_almacenada==contraseña1_escrita:
    print("pass")
else: 
    print("No puedes pasar")
    

#----------------------------------------------------------------#

ingreso_mensual=7200
gasto_mensual = 8000

#If anidados y elif 
if ingreso_mensual > 100000:
    if ingreso_mensual-gasto_mensual < 0: 
        print("estas mal")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bien, estas bien")
    else: 
        print("estas gastandop mucho, hay que ver si alcanza")
        
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")

elif ingreso_mensual > 500:
    print("estaas bien en tu pueblo")

elif ingreso_mensual > 200:
    print("no salgas de tu pueblo") 
    
else:
    print("No salgas de tu pueblo")                        
       
    