import random, delitos_años
    
def CreacionCarcel(): 
    """Funcion que se encarga de la creacion de una matriz con medidas especificadas por el usuario, 
    que se utilizara como plantilla para el sistema penitenciario organizado."""

    c_celdas = int(input("Ingrese la capacidad de cada celda: ")) # Capacidad por celda
    while c_celdas<=0:
        print("Cantidad invalida, ingrese un numero mayor a 0.")
        c_celdas = int(input("Ingrese la capacidad de cada celda: "))

    c_pisos = int(input("Ingrese la cantidad de celdas por piso: ")) # Capacidad por piso (cantidad de celdas)
    while c_pisos<=0:
        print("Cantidad invalida, ingrese un numero mayor a 0.")
        c_pisos = int(input("Ingrese la cantidad de celdas por piso: "))

    c_carcel = int(input("Ingrese la cantidad de pisos: ")) #Cantidad de pisos
    while c_carcel<=0:
        print("Cantidad invalida, ingrese un numero mayor a 0.")
        c_carcel = int(input("Ingrese la cantidad de pisos: "))
    

    carcel = [] # Carcel que tendra de dimension
    carcel = [[] for i in range(c_carcel)] #Creacion de los pisos.
    for i in range(len(carcel)): 
        carcel[i] = [[] for j in range(c_pisos)] #Creacion de las celdas

        """Por lo tanto, i representa el piso, y k representa la ubicacion de la celda"""
        for k in range(len(carcel[i])):
            carcel[i][k] = [0 for j in range(c_celdas)] #Creacion de los espacios por celda. Donde 0 representa un espacio vacio

    #Impresion de valores para orientarse:
    print("A cotinuacion, una representacion grafica de su carcel:")
    print()
    print("Cantidad de pisos: {}".format(c_carcel))
    print("Cantidad de celdas por piso: {}".format(c_pisos))
    print("Cantidad de presos por celda: {}".format(c_celdas))
    print()
    ImpresionMatriz(carcel)
    
    return carcel

def Divisiones(carcel):
    """Funcion que se encargara de establecer los lapsos de tiempo en años en los que se basara
      la division de los pisos de la prision.
      Esto lo consigue dividiendo la distribucion en partes iguales por piso.
      
      Parametro: matriz de la prision."""
    
    division = 1/len(carcel)#Medida que se va a usar para dividir la cantidad de años totales en proporcion a los pisos
    d_pisos = [] # Lista que va a referenciar los años para dividir los pisos.

    for i in range(len(carcel)): #Se usa una lista que va a contener valores de tiempo en referencia al piso.
        d_pisos.append(25*division*(i+1))
    
    return d_pisos

def CantidadPresos(espacio):
    """Funcion que se encargara de delimitar la cantidad de presos que se trasladen a la prision. 
    Siendo la proporcion de dos tercios.
    
    Parametro: Disponibilidad total maxima de la prision."""
    
    presos = 0 
    for i in range(espacio): #Cantidad de presos que ocupan la carcel, 2 de cada 3
        if random.randint(1,3)!=2:
            presos+=1
    return presos

def DimensionesCarcel(plantilla):
    """Funcion que se encarga de devolver el orden de la matriz tridimensional.
    Se utilza para no reescribir lineas de codigo.

    Parametro: Matriz de prision."""

    # Almacena todas las dimensiones de la matriz
    pisos = len(plantilla)
    celdas = len(plantilla[0])
    espacio = len(plantilla[0][0])

    return pisos,celdas,espacio

def DisponibilidadCarcel(plantilla):
    """Funcion que se encarga de mostrar la disponibilidad total maxima dentro de la prision.
    Se utiliza para separar codigo que no cumple la funcion especifica del programa.
    
    Parametro: Matriz de prision."""
    c_espacio, c_celdas, c_pisos = DimensionesCarcel(plantilla) # Cantidad de espacio, celdas y pisos.
    capacidad = lambda espacio, celdas, pisos: espacio*celdas*pisos #Funcion lambda que muestra el espacio disponible en la carcel
    disponible = capacidad(c_celdas,c_espacio,c_pisos) # La totalidad del espacio en la matriz
    return disponible

def InfoPresos(disponibilidad):
    """Funcion que se encarga de individualizar a cada uno de los presos que son trasladados a la prision.
    Esto, asignando un numero especifico, un delito, y un tiempo de condena determinado a cada individuo.
    
    Parametro: Presos trasladados a la prision."""

    l_presos = [] #Lista donde se almacenaran los numeros de preso
    l_crimenes = [] #Lista donde se almacenaran los crimenes de los respectivos presos
    l_condenas = [] #Lista donde se almacenaran los tiempos de condena de los respectivos presos

    cantidad = CantidadPresos(disponibilidad) #Cantidad de presos trasladados 

    for i in range(cantidad):
        delito = delitos_años.aleatorio_delito() #Delito cometido
        legajo = delitos_años.numero_preso(delito) #Legajo del preso, en relacion con el crimen cometido
        while legajo in l_presos:
            legajo = delitos_años.numero_preso(delito)
        t_condena = delitos_años.cantidad_años(delito) #Tiempo de condena
        
        l_presos.append(legajo)
        l_crimenes.append(delito)
        l_condenas.append(t_condena)
    
    return l_presos,l_crimenes,l_condenas

def SistemaPenitenciario(base, l_presos, l_condenas):
    """Funcion que se encarga de organizar a los presos segun su delito cometido y el tiempo de condena.
    Esto lo consigue aprovechando sus legajos distintivos para su inserccion, 
    y basando su eleccion del piso en un margen de tiempo.
    
    Parametros: - matriz de prision.
                - lista con los numeros de presos.
                - lista con las condenas de los presos."""
    
    carcel = []
    carcel.extend(base) #Se utiliza una lista nueva que contendra de plantilla a la matriz tridimensional creada previamente, para no modificarla.
    tiempos = Divisiones(carcel) #Lista que contiene las divisiones de tiempo en las que se basaran los pisos.
    c_pisos,c_celdas, c_espacio = DimensionesCarcel(base)
    cantidad = len(l_presos) #Cantidad de presos
    l_indices = []


    for i in range(cantidad): #Asignacion de preso a carcel
        ocupado = False #Variable que anulara el ciclo de ser ocupado un lugar.
        legajo = l_presos[i]
        t_condena = l_condenas[i]

        #Se inicia un proceso en el que se separan a los presos en funcion del piso y se agruparan en funcion del crimen que cometieron

        for j in range(len(tiempos)):
            # j recorrera todos los valores de referencia en d_pisos, de menor a mayor, por lo que si es menor, significia que se encuentra dentro de ester rango
            if t_condena<tiempos[j] and not ocupado:
                if legajo>=3000: # Los crimenes mas graves se agruparan en las celdas mas lejanas
                    n = c_celdas-1 #n es una variable que servira de subindice para ubicar la celda
                    while n != -1 and not ocupado:
                        c=0 #Variable que servira de contador
                        while c<c_espacio and not ocupado:
                            if carcel[j][n][c]==0:
                                carcel[j][n][c] = legajo
                                l_indices.append([j,n])
                                ocupado = True #Se cancelan los ciclos porque ya se realizo la operacion deseada
                            else:
                                c+=1
                        n-=1
                        
                else: #Los crimenes menos graves se agruparan en las celdas mas cercadnas  
                    n = 0 #n es una variable que servira de subindice para ubicar la celda
                    while n < c_celdas and not ocupado:
                        c=0 #Variable que servira de contador
                        while c<c_espacio and not ocupado:
                            if carcel[j][n][c]==0:
                                carcel[j][n][c] = legajo
                                l_indices.append([j,n])
                                ocupado = True #Se cancelan los ciclos porque ya se realizo la operacion deseada
                            else:
                                c+=1
                        n+=1
    print()
    print("A continuacion, el sistema penitenciario organizado: ")
    print()
    ImpresionMatriz(carcel)

    return carcel, l_indices

def AccesoLegajo(l_presos,l_delitos,l_condenas, carcel):
    """Funcion que se encarga de que el usuario pueda acceder a la informacion de un preso ingresado por teclado.
    Esto con la utilizacion de listas que referencian a los presos y listas paralelas que referencien su informacion.
    
    Parametros: - Lista con numeros de preso.
                - Lista con delitos de los presos.
                - Lista con los tiempos de condena de los presos.
                - matriz con la ubicacion de cada preso."""
    
    print()
    preso = int(input("Ingrese el legajo del que quiere saber los antecedentes: ")) #Se ingresa el numero de preso
    while preso not in l_presos:
        preso = int(input("Error, elija un legajo existente: "))

    indice = l_presos.index(preso) #Se obtiene el indice en la lista de presos
    delito, condena = l_delitos[indice],l_condenas[indice] #En relacion al indice se obtienen todos los datos

    #Se imrpime el numero de prisionero, el delito cometido, su condena y su alojamiento en la prision.
    print()
    print("El prisionero {} ha sido detenido por {} y fue condenado por {} años".format(preso,delito,condena))
    print("El mismo se encuentra encerrado en el piso {}, sobre la celda {}".format((carcel[indice][0])+1,(carcel[indice][1])+1)) #Carcel es la lista de indices

def RevisionCarcel(carcel):
    """Esta funcion permite al usuario acceder a informacion especifica sobre la carcel.

    Parametros: Matriz de Carcel procesada."""
    
    # El usuario ingresa si desea acceder a informacion de la carcel o no.
    eleccion = ""
    while eleccion.capitalize()!= "No":
        print()
        eleccion = input("Desea saber algo sobre su carcel? (Responder con si o no): ")
        while eleccion.capitalize() != "Si" and eleccion.capitalize()!= "No":
            eleccion = input("Error, solo puede responder si o no: ")

        #En caso afirmativo, debe elegir una de las opciones dadas.
        if eleccion.capitalize() == "Si":
            print("Que desea saber sobre la carcel? (Ingrese 1,2,3,4)")
            print()
            print("1 = Totalidad de presos")
            print("2 = Presos de un piso.")
            print("3 = Presos de una celda.")
            print("4 = Presos mas propensos a ser peligrosos.")
            n = int(input("Ingrese su eleccion: "))
            while n<1 or n>4:
                print(("Error, ingrese solo los caracteres especificados."))
                print()
                print("1 = Totalidad de presos")
                print("2 = Presos de un piso.")
                print("3 = Presos de una celda.")
                print("4 = Presos considerados peligrosos.")
                n = int(input("Ingrese su eleccion: "))
            
            #Caso 1: Impresion detallada de la carcel.
            if n==1:
                for i in range(len(carcel)):
                    print()
                    print(f"Piso {i+1}: ")
                    for j in range(len(carcel[i])):
                        print(f"Celda {j+1}: {carcel[i][j]}")
                        print()
            
            #Caso 2: Impresion detallada de un piso de la carcel.
            elif n==2:
                n = int(input("Ingrese el numero de piso: "))
                while n<1 or n>len(carcel):
                    n = int(input("Error, ingrese un piso que exista: "))
                print()
                print(f"Piso: {n}")
                for i in range(len(carcel[n-1])):
                    print(f"Celda {i+1}: {carcel[n-1][i]}")
                    print()

            #Caso 3: Impresion detallada de una celda especifica.
            elif n==3:
                n = int(input("Ingrese el numero de piso: "))
                while n<1 or n>len(carcel):
                    n = int(input("Error, ingrese un piso que exista: "))
                n2 = int(input("Ingrese el numero de celda: "))
                while n2 < 1 or n2>len(carcel[n-1]):
                    n2 = int(input("Error, ingrese una celda que exista: "))
                
                print(f"En la celda {n2} del piso {n} se encuentran los presos: {carcel[n-1][n2-1]}")
            
            #Caso 4: Impresion de las celdas mas lejanas, donde se alojan los presos mas peligrosos.
            elif n==4:
                peligro = len(carcel)//2
                for i in range(len(carcel)):
                    print()
                    print(f"Piso {i+1}: ")
                    print(carcel[i][peligro:])

def ImpresionMatriz(matriz):
    pisos, celdas, espacio = DimensionesCarcel(matriz)
    
    print("Desea ver su matriz impresa de forma detallada? Responda con si o no. ")
    print("ADVERTENCIA: De tener una cantidad de celdas y espacio superior a 4, podria distorsionarse este metodo de visualizacion dadas las limitaciones de espacio.")
    eleccion = input("")
    if eleccion.capitalize()=="Si": 
        ancho = 32
        cadena = "".rjust(20)
        for i in range(celdas):
            cadena += f"| Celda {i+1} |".center(ancho)
        
        print(cadena)
        for i in range(pisos):
            cadena = f"| Piso {i+1} |".rjust(20)
            for j in range(celdas):
                cadena += f"| {matriz[i][j]} |".center(ancho)
            print(cadena)
    else:
        for i in range(pisos):
            print(f"Piso {i+1}: {matriz[i]}")
          
    
    print()

def main():
    """El programa principal se encarga de permitirle al usuario buscar un determinado numero de preso, 
    para que el mismo pueda acceder a su informacion."""

    base = CreacionCarcel() #Modelo de carcel a utilizar
    disp = DisponibilidadCarcel(base) #Disponibilidad total de la carcel
    presos, delitos, condenas = InfoPresos(disp) #Listas donde se referenciara a cada uno de los presos
    carcel, indices = SistemaPenitenciario(base,presos,condenas) #Sistema penitenciario organizado. Variables que toman la carcel y una lista con los indices
    RevisionCarcel(carcel)
    n = ""

    # Consulta al usuario si desea buscar informacion sobre un preso, en caso afirmativo, lo dirigira a una funcion
    while n.capitalize()!= "No":
        print()
        n = input("Desea buscar datos sobre algun preso? (responder con si o no): ")
        while n.capitalize() != "Si" and n.capitalize()!= "No":
            n = input("Error, solo puede responder si o no: ")

        if n.capitalize() == "Si":
            AccesoLegajo(presos,delitos,condenas, indices)
    
    print("Programa finalizado.")

if __name__=="__main__":
    main()