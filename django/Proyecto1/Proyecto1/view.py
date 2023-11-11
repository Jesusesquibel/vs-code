from django.http import HttpResponse

def saludo(request): #primera vista 
    
    return HttpResponse("Hola Jesus Esquibeel")

def despedida(request): # parte de la primera vista
  
    return HttpResponse("ve con jairo a dormir ")