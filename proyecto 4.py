import Diseño_carcel,Datos_prisioneros
def CreacionCarcel():
    '''Funcion que creara un diccionario que alojara la carcel a utilizar en el programa'''
    try:
        d_carcel = () #Tupla que contendra las dimensiones de la carcel.
        Diseño_carcel.DimensionesCarcel() #Funcion que registrara en un archivo datos sobre la carcel
        lectura = open("dimensiones.txt","rt")
        linea = lectura.readline() #Variable que contendra el valor de una linea leida en el archivo
        while linea: #Siempre que la linea del archivo tenga un valor. se seguira con la iteracion
            d_carcel += int(linea.rstrip()),
            linea = lectura.readline() 
        lectura.close()
        pisos,celdas,espacio = d_carcel

        #Creacion de la carcel a partir de un diccionario por comprension, que contendra otro del mismo tipo, y una lista por comprension
        carcel = {i+1:{j+1: [0 for k in range(espacio)] for j in range(celdas)} for i in range(pisos)}
        return carcel, d_carcel #Se retorna el diccionario que contiene la carcel junto con la tupla de sus dimensiones.
    except IOError: #En caso de un Error durante el manejo de archivos:
        print("No se encontro el archivo de lectura")
        
def ImpresionCarcel(carcel):
    """Funcion que imprime de forma clara la carcel con sus respectivos pisos, celdas y espacios.
    
    Parametros: carcel: Diccionario que contendra los datos de la carcel."""
    for i in carcel:
        print(f"Piso {i}: ",end="|") #Parte izquierda
        for j in carcel[i]:
            print(f"{carcel[i][j]}",end="-") #Parte derecha, sin saltos de linea.
        print("") #Salto de linea cuando se termina de recorrer un piso.
    print("") #Salto de linea que deja un espacio para la proxima impresion.

def EscrituraArchivo(l_datos,d_carcel,l_ubicacion):
    """Funcion que se encargara de la grabacion de archivos con datos no incluidos en los previamente establecidos
    
    Parametros: 1- l_datos: Lista con tuplas respecto a los datos de cada uno de los prisioneros
                2- d_carcel: Tupla que contendra las dimensiones de la carcel generada
                3- l_ubicacion: Lista de tuplas correspondientes al piso y a la celda de cada prisionero."""
    # Grabacion de archivos
    try:
        registro_pisos = open("piso.txt","wt")
        for i in l_ubicacion:
            registro_pisos.write(f"{i[0]}\n")
        registro_pisos.close()

        registro_celdas = open("celda.txt","wt")
        for i in l_ubicacion:
            registro_celdas.write(f"{i[1]}\n")
        registro_celdas.close()

        registro_utilizadas = open("celdas_usadas.txt","wt")
        presos_max,celdas_ocupadas = d_carcel[0]*d_carcel[1]*d_carcel[2],len(l_ubicacion)
        registro_utilizadas.write(f"{presos_max}\n{celdas_ocupadas}\n{presos_max-celdas_ocupadas}") 
        registro_utilizadas.close()

        #Grabacion de un archivo completo que presentara todos los datos almacenados en el programa
        registro_datos = open("datos_exactos.txt","wt")
        for i in range(len(l_datos)):
            registro_datos.write(f"Prisionero: {l_datos[i][0]}, Numero de preso: {i+1}, causa de arresto: {l_datos[i][1]}, tiempo de condena: {l_datos[i][2]}, ubicacion: {l_ubicacion[i][0]} piso, {l_ubicacion[i][1]} celda.\n")
        registro_datos.close()

    except IOError:
        print("Error en el acceso a los archivos de registro.")

def InformacionPrisioneros():
    """Funcion que se encargara de leer todos los archivos grabados por los modulos y almacenar su informacion
    en variables a las que se le dara uso posteriormente en el programa."""
    #Lectura de archivos:
    try:
        t_presos = () #Tupla que contendra los legajos de los prisioneros
        t_crimenes = () #Tupla que contendra los crimenes cometidos por cada prisionero
        t_tiempo = () #Tupla que contendra los tiempos de condena de cada prisionero

        lectura_legajos = open("legajos.txt","rt")
        linea = lectura_legajos.readline() #Variable que contendra el valor de una linea leida en el archivo
        while linea: #Siempre que la linea del archivo tenga un valor. se seguira con la iteracion
            t_presos += int(linea.rstrip()), #Se agrega el respectivo valor a la tupla, eliminando los saltos de linea.
            linea = lectura_legajos.readline()
        lectura_legajos.close()

        lectura_crimenes = open("crimenes.txt","rt")
        linea = lectura_crimenes.readline() #Variable que contendra el valor de una linea leida en el archivo
        while linea: #Siempre que la linea del archivo tenga un valor. se seguira con la iteracion
            t_crimenes += linea.rstrip(), #Se agrega el respectivo valor a la tupla, eliminando los saltos de linea.
            linea = lectura_crimenes.readline()  
        lectura_crimenes.close()

        lectura_tiempo = open("tiempo.txt","rt")
        linea = lectura_tiempo.readline() #Variable que contendra el valor de una linea leida en el archivo
        while linea: #Siempre que la linea del archivo tenga un valor. se seguira con la iteracion
            t_tiempo += int(linea.rstrip()), #Se agrega el respectivo valor a la tupla, eliminando los saltos de linea.
            linea = lectura_tiempo.readline() 
        lectura_tiempo.close()

        return t_presos,t_crimenes,t_tiempo

    except IOError:
        print("No se pudo acceder a los archivos requeridos.")

def SistemaPenitenciario():
    """Funcion que se encarga de organizar a los prisioneros en las ubicaciones disponibles de la carcel
    
    En la misma se llevaran a cabo los algoritmos de creacion de la carcel, individualizacion de los presos,
    y registrado en los archivos."""
    try:
        class Ocupado(Exception): #Creacion de una excepcion para romper el algoritmo de ordenamiento.
            pass
        carcel, d_carcel = CreacionCarcel() #Se almacena la carcel y la tupla con las dimensiones de la misma.
        pisos,celdas,espacio = d_carcel #Desempaquetado de la tupla.
        ImpresionCarcel(carcel) #Se imprime la carcel sin presos alojados.
        Datos_prisioneros.IndividualizacionPresos(d_carcel)
        t_presos,t_crimenes,t_tiempo = InformacionPrisioneros() #Se registran en variables la informacion de los archivos previos
        l_datos = [(t_presos[i],t_crimenes[i],t_tiempo[i]) for i in range(len(t_presos))] #Creacion de una lista que contendra tuplas con la informacion particular de cada prisionero
    
        l_ubicacion = [] #Lista que contendra en tuplas la ubicacion de cada prisionero, el primer valor correspondiendo al piso y el segundo a la celda.
        parametro_tiempo = 14//pisos #Se asigna el valor que se va a usar como parametro para la division de pisos
        l_parametro_tiempo = [parametro_tiempo*i for i in range(pisos)] #Lista que asigna valores de referencia que se van a utilizar como parametros para la division de pisos.
        parametro_legajo = 50_000 #Parametro utilizado para jerarquizar la ocupacion de celdas.
        """Se inicia el algoritmo de ordenamiento"""
        for i in t_presos: #Ciclo for que toma el valor de cada uno de los legajos en t_presos
            try: #Bloque de codigo protegido
                tiempo = t_tiempo[t_presos.index(i)] #Se almacena el tiempo de condena correspondiente del preso
                for j in range(len(l_parametro_tiempo),0,-1): #Se recorre la lista de parametros en reversa, para identificar dentro de que rango se encuentra el prisionero.
                    #La utilidad de recorrerla en reversa radica en que si el piso se encuentra complemtamente ocupado, lo alojara en el siguiente del nivel inferior
                    if tiempo>l_parametro_tiempo[j-1]: #Si se encuentra en el rango, se prosigue:
                        for k in range(j,pisos+1): #Se recorren los pisos desde el parametro para arriba, buscando ubicaciones desocupadas.
                            if i>parametro_legajo: #Si el legajo supera el parametro de legajo establecido:
                                for l in range(celdas,0,-1):#Se recorren las celdas en reversa.
                                    for m in range(espacio-1,-1,-1):#Se recorre el espacio en reversa.
                                        if carcel[k][l][m]==0: #Si el espacio no tiene un preso alojado:
                                            carcel[k][l][m] = i #Se sobreescribe el preso sobre el espacio.
                                            l_ubicacion.append((k,l)) #Se agrega la ubicacion a la variable
                                            raise Ocupado #Se llama al error "Ocupado", creado al principio de la funcion
                            else:
                                for l in range(1,celdas+1): #Se recorre la celda normalmente
                                    for m in range(espacio): #Se recorre el espacio normalmente
                                        if carcel[k][l][m]==0: #Si el espacio no tiene un preso alojado:
                                            carcel[k][l][m] = i #Se sobreescribe el preso sobre el espacio.
                                            l_ubicacion.append((k,l)) #Se agrega la ubicacion a la variable
                                            raise Ocupado #Se llama al error "Ocupado", creado al principio de la funcion
            except Ocupado: #Cuando se llama al error, se continua con el siguiente preso. Forma sencilla de romper los ciclos
                continue
        
        ImpresionCarcel(carcel) #Se imprime la carcel en consola nuevamente, pero con los presos asignados.
        EscrituraArchivo(l_datos,d_carcel,l_ubicacion) #Se graban todos los datos en el archivo "Registro_carcel.txt"
        return l_datos,t_presos #Se retorna la lista con las tuplas de datos de los presos, y la tupla con los legajos.
    
    except TypeError: #No se recibieron los parametros esperados
        print("No se pudo trabajar con los archivos necesarios.")
        
def AccesoLegajo(t_presos,l_datos):
    '''Funcion que permite al usuario acceder a la informacion especifica de un preso ingresado por teclado.
    
    Los diferentes legajos pueden visualizarse en el archivo "Registro_carcel.txt" o en la consola.
    
    Parametros: 1- t_presos: Tupla que contendra los legajos de los presos
                2- l_datos: Lista que contendra los datos empaquetados correspondientes a cada prisionero.'''
    try:
        registro_accesos = open("accedidos.txt","wt") #Archivo en el que se grabara la totalidad de presos a los que se accedio
        class Salida(Exception): #Creacion de una excepcion que se utilizara para finalizar el programa.
                pass
        while True:
            try:
                op = int(input("\nIngrese el legajo del prisionero del que desea saber informacion o -1 si desea finalizar: ")) #Se le permite al usuario decidir si quiere acceder a informacion especifica de los prisioneros o no.
                assert op in t_presos or op==-1 #Si se ingresa un legajo inexistente, se genera un error.
                if op==-1: #Si se ingresa -1, se finaliza el programa.
                    registro_accesos.close()
                    raise Salida
                indice = t_presos.index(op) #Indice correspondiente al prisionero.
                print(f"\nEl prisionero {op} es el numero {indice+1}, fue arrestado por {l_datos[indice][1]} y cuenta con un tiempo de condena de {l_datos[indice][2]} años.")
                registro_accesos.write(f"{op}\n") #Se registra el legajo en el archivo.
            except ValueError: #Si se ingresa un valor no compatible con int:
                print("Error, los legajos estan conformados unicamente de numeros.")
            except AssertionError: #Si se ingresa un legajo inexistente
                print("El prisionero no existe. Reingrese.")
            except Salida: #Finaliza el programa.
                print("Busqueda de legajos finalizada.")
                break #Se rompe el ciclo y finaliza la funcion.
    except IOError:
        print("Error en la apertura del archivo.")
def main():
    """Programa principal: permite al usuario acceder a informacion especifica dentro de la variedad de prisioneros
      generados:"""
    """Se acciona el algoritmo principal que permite la generacion, individualizacion, y distribucion de prisioneros.
       Se recibe una lista con sus datos empaquetados, y una tupla paralela con sus legajos."""
    try:
        l_datos, t_presos = SistemaPenitenciario() #Funcion en la que se creara la carcel y se le asignaran los presos respecto a lo que hayan cometido
        while True: #Se continuara con el ciclo hasta que se ingrese "No".
            try:
                op = input('Desea acceder a la informacion de un prisionero en particular? Responda con "Si" o "No": \n ') #Se pide el ingreso de datos por teclado.
                op = op.lower() #Se pasa todo a minuscula para evitar distincion por lo mismo.
                assert op=="si" or op=="no" #Si se ingresa una opcion que no sea si o no, se genera un error.
                if op=="si": #Si se ingresa que si
                    AccesoLegajo(t_presos,l_datos) #Se llama a la funcion que permitira acceder a estos datos
                print("Gracias por usar el programa.") 
                break #Se finaliza el programa.
            except AssertionError: #Se vuelve a preguntar en caso de una respuesta invalida.
                print('Respuesta invalida, responda con "Si" o "No".')
    except TypeError:
        print("No se pudo ejecutar el programa debido a un error en la lectura o escritura de archivos.")
if __name__=="__main__":
    main()