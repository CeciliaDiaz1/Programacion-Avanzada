#Programa (lee archivos csv)

#Se usa para acceder a archivos que son de tipo CSV
import csv

#El wwith hace refernecia a a que estare trbajando con "tal" archivo.
#Cuando diga archivo.csv hablo de lo que contiene el archivo seleccionado. ("AnalisisCOVID19")
with open('AnalisisCOVID19.txt') as archivo_csv:
    #Permite leer el contenido del archivo.
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    contador_lineas = 0
    #Lee el archivo secuencialmente (tal y como esta)
    for linea_datos in lector_csv:
        #Si el contador esta en 0, significa que estamos en la primera linea del archivo.
        if contador_lineas == 0:
            #Genera un lista con los datos de la linea en la que se este, separados por una coma
            print(f'Los nombres de las columnas son {", ".join(linea_datos)}')
        else:
             #Muestra dato por dato de la linea en la que estamos.
            print(f'\tFECHA: {linea_datos[0]} .')
            print(f'\tNUEVOS CONTAGIOS: {linea_datos[1]}.')
            print(f'\tNUEVOS FALLECIMIENTOS: {linea_datos[2]}.')
            print(f'\tPAÍS: {linea_datos[3]}.')
            print(f'\t--------------------------------------------------------')
        #Se coloca fuera para que funcione sin importar lo que pase (if o else).
        contador_lineas += 1
    print(f'Procesadas {contador_lineas} lineas.')