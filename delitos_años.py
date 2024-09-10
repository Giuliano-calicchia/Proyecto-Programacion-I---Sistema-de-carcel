import random

def aleatorio_delito():
    delito = ["Homicidio", "Robo", "Trafico de drogas", "Abuso sexual", "Secuestro"]
    delito_azar = random.randint(0,len(delito)-1)
    delito_final = delito[delito_azar]

    return delito_final

def cantidad_años(x):
    
    if x == "Homicidio":
        años = random.randint(8,25)
    
    elif x == "Robo":
        años = random.randint(3,10)

    elif x == "Trafico de drogas":
        años = random.randint(4,15)

    elif x == "Abuso sexual":
        años = random.randint(4,10)

    elif x == "Secuestro":
        años = random.randint(3,8)
    
    return años

def numero_preso(x):
    if x == "Robo":
        num = random.randint(1000,1999)
    
    elif x == "Trafico de drogas":
        num = random.randint(2000,2999)

    elif x == "Abuso sexual":
        num = random.randint(3000,3999)

    elif x == "Homicidio":
        num = random.randint(4000,4999)

    elif x == "Secuestro":
        num = random.randint(5000,5999)
    
    return num

