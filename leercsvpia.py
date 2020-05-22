#Programa (lee archivos csv)

# Se importa la librería para tipo fecha.
import datetime

#Se usa para acceder a archivos que son de tipo CSV
import csv

# Clase Contacto.
class Contacto:

# Propiedades de la clase.
  def __init__(self, nickname, nombre,correo,telefono,fechanacimiento,gastos):
    self.nickname=nickname
    self.nombre=nombre
    self.correo=correo
    self.telefono= telefono
    self.fechanacimiento=fechanacimiento
    self.gastos=gastos

#El wwith hace refernecia a a que estare trbajando con "tal" archivo.
#Cuando diga archivo.csv hablo de lo que contiene el archivo seleccionado. ("AnalisisCOVID19")
with open('contactos_mobil.csv') as archivo_csv:
    #Permite leer el contenido del archivo.
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    contador_lineas = 0
    #Se crea una lista vacía llamada objetos.
    Contactos = []
    #Lee el archivo secuencialmente (tal y como esta)
    for linea_datos in lector_csv:
        #Si el contador esta en 0, significa que estamos en la primera linea del archivo.
        if contador_lineas == 0:
            #Genera un lista con los datos de la linea en la que se este, separados por una coma
            print(f'Los nombres de las columnas son {", ".join(linea_datos)}')
        else:
            #Muestra dato por dato de la linea en la que estamos.
            print(f'\tNickname: {linea_datos[0]} .')
            print(f'\tNombre: {linea_datos[1]}.')
            print(f'\tCoreo: {linea_datos[2]}.')
            print(f'\tTelefono: {linea_datos[3]}.')
            print(f'\tFecha nacimiento: {linea_datos[4]}.')
            print(f'\tGatos: {linea_datos[5]}.')
            print(f'\t--------------------------------------------------------')
            objeto_temporal = Contacto (input({linea_datos[0]}), str({linea_datos[1]}), str({linea_datos[2]}), int({linea_datos[3]}), datatime.datatime({linea_datos[4]}), int ({linea_datos[5]}))
            Contactos.append(objeto_temporal)  
        #Se coloca fuera para que funcione sin importar lo que pase (if o else).
        contador_lineas += 1
    print(f'Procesadas {contador_lineas} lineas.')
    