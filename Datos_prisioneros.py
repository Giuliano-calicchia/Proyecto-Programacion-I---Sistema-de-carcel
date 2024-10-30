import random
"""Modulo que generara la cantidad de presos ingresada por el usuario previamente, y registrara todos sus datos en archivos csv"""


def IndividualizacionPresos(d_carcel):
    """Funcion que se encargara de individualizar a cada uno de los presos que conforman la carcel, asignandoles un legajo, un numero
    de prisionero, un crimen cometido, y un tiempo de condena en años. Para luego, registrar todos estos datos en un archivo

    
    Parametros: d_carcel: Tupla que contiene las dimensiones de la carcel, va a ser desempaquetada."""
    
    pisos,celdas,espacio = d_carcel #Se desempaqueta la tupla.
    presos_max = pisos*celdas*espacio #Se calcula el maximo espacio posible a ocupar.
    presos_max = random.randint(presos_max//2,presos_max) #De este maximo, se genera un numero aleatorio entre su mitad y el maximo.
    presos_max = presos_max+1 if presos_max==0 else presos_max #Si presos_max es 0 porque el usuario ingreso el valor de 1, para no generar error en el random, se añadira 1 preso maximo en otra linea
    #Lista con crimenes
    crimenes = ["Consumo de sustancias en lugares publicos", "Vandalismo","Porte de sustancias ilegales","Hurto menor","Invasion a la propiedad privada","Robo a mano armada","Asalto con herido","Asesinato","Secuestro"] #Lista de crimenes
    t_presos = set() #Creacion de un conjunto que posteriormente sera una tupla con los legajos de los presos.
    t_crimenes = () #Creacion de una tupla que contendra los crimenes de cada preso. Tupla paralela a t_presos.
    t_tiempo = () #Creacion de una tupla que contendra los años de condena de cada preso. Tupla paralela a t_presos.

    """Asignacion de valores a cada una de las tuplas y lista creadas previamente"""
    while len(t_presos)<presos_max: #Mientras el conjunto no alcance la cantidad de presos generada previamente, se seguiran agregando valores.
        legajo = (random.randint(10000,99999))
        t_presos.add(legajo)
    t_presos = tuple(t_presos)
    #El crimen cometido por el preso estara correlacionado con su legajo y su tiempo de condena.
    for i in range(len(t_presos)):
        crimen = (t_presos[i]//10000)-1
        t_crimenes += (crimenes[crimen],)
        t_tiempo += (random.randint(crimen+1, crimen + (random.randint(2,6))),)
    
    #Grabacion de datos de los prisioneros.
    grabacion_legajos = open("legajos.txt","wt")
    for i in t_presos:
        grabacion_legajos.write(f"{i},")
    grabacion_legajos.close()
    grabacion_crimenes = open("crimenes.txt","wt")
    for i in t_crimenes:
        grabacion_crimenes.write(f"{i},")
    grabacion_crimenes.close()
    grabacion_tiempo = open("tiempo.txt","wt")
    for i in t_tiempo:
        grabacion_tiempo.write(f"{i},")
    grabacion_tiempo.close()
