#Programa que lea archivos CSV  y carga en un objeto y lo almacena en una lista.

#Se usa para poder acceder a archviso tipo CSV
import csv

#Libreria para manejar datos tipo datetime
import datetime

#Clase incidentes con sus propiedades.
class  Incidente():
    def __init__(self,FECHA, CASOS, MUERTES, COUNTRY):
        self.FECHA = FECHA
        self.CASOS = CASOS
        self.MUERTES = MUERTES
        self.COUNTRY = COUNTRY

with open('AnalisisCOVID19.txt') as archivo_csv:
    #Permite leer el contenido del archivo.
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    contador_lineas = 0
    # Lista vacía para guardar los incidentes.
    lista_incidentes = []
    #Lee el archivo secuencialmente (tal y como esta)
    for linea_datos in lector_csv:
        #Si el contador esta en 0, estamos en la primera linea del archivo
        # pero no se guarda nada en la lista.
        if contador_lineas == 0:
            #Genera un lista con los datos de la linea en la que se este, separados por una coma
            print(f'Los nombres de las columnas son {", ".join(linea_datos)}')
        else:
            #Si son datos; genero una instancia de la clase Incidente.
            objeto_temporal = Incidente (str({linea_datos[0]}), int({linea_datos[1]}), int({linea_datos[2]}), str({linea_datos[3]}))
            lista_incidentes.append(objeto_temporal)  
        contador_lineas += 1 
    #Lo que hace esta ultima linea es contar cuantas lineas hay en nuestra lista de incidentes.
    print(f'Procesadas {len(lista_incidentes)} lineas.')