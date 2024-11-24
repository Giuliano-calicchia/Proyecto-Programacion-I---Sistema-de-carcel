"""Modulo que se encargara de la creacion del diccionario que alojara la carcel, y grabara en un archivo datos
respecto a la misma."""

def DimensionesCarcel():
    """Funcion que se encarga de la grabacion de las especificaciones del usuario respecto a la carcel."""
    class NoNatural(Exception): #Se crea una excepcion para detectar el ingreso de numeros no naturales
        pass

    # Ciclo infinito para simplificar codigo, se rompera unicamente si se ingresan los valores correctos.
    while True:    
        try:
            pisos = float(input("Ingrese la cantidad de pisos: ")) #Cantidad de pisos.
            assert int(pisos*10)==int(pisos)*10 #Comprobacion.
            if pisos<1: #Si se ingresa un numero no natural, se genera error.
                raise NoNatural
            celdas = float(input("Ingrese la cantidad de celdas: ")) #Cantidad de celdas.
            assert int(celdas*10)==int(celdas)*10 #Comprobacion.
            if celdas<1: #Si se ingresa un numero no natural, se genera error.
                raise NoNatural
            espacio = float(input("Ingrese el espacio por celda: ")) #Cantidad de espacio.
            assert int(espacio*10)==int(espacio)*10 #Comprobacion.
            if espacio<1: #Si se ingresa un numero no natural, se genera error.
                raise NoNatural
            #Pasa todas las variables a un valor valido para lo que se utilizara posteriormente
            pisos = int(pisos)
            celdas = int(celdas)
            espacio = int(espacio)

            #Grabado de archivos con informacion respecto a la carcel        
            grabado = open("dimensiones.txt","wt")
            grabado.write(f"{pisos}\n{celdas}\n{espacio}\n") #Se registran las dimensiones de la carcel, separadas por salto de linea, para evitar la carga del archivo completo en memoria posteriormente
            grabado.close()
            break
            
        except ValueError: #Si se ingresa un valor invalido: 
            print("Se ingreso una cadena de caracteres. Escribalo en numeros por favor.")
        except AssertionError: #Si se ingresa un numero con coma: 
            print("Se ingreso un numero flotante. Por favor, re-ingrese los datos.")
        except NoNatural: #Se vuelven a pedir los datos.
            print("Solo se admiten numeros naturales.")
        except IOError:
            print("Se ha producido un error durante la creacion del archivo")
            break

            
    
    
