#Se usa para la validación de expresiones regulares
import re
#Esta funcion se usa para poder trabajar con datos tipo datetime
import datetime

#Se declara una variable para colocar los datos que se vayan preguntando, en caso de que este sea correcto.
captura=""

def askandcheck(_patron,_pregunta="Dame un dato: "):
    #Se declara que la variable "captura" es global, para que el programa no o tome como si solo fuera local para realizar esta función.
    global captura
    while True:
        _fxvalor = input(_pregunta)
        coincide = re.search(_patron, _fxvalor)
        if (coincide):
          #Si el dato colocado por el usuario el usuario es correcto el programa se detendra.
            captura= _fxvalor
            break
        else:
          #De lo contrario imprimira el siguiente mensaje, y preguntara de nuevo.
            print("El dato no es correcto. Intenta de nuevo.")

#Convierte una expresión de año, mes y dia a datetime
def strtodate(_dtoconv):
    return datetime.datetime(int(_dtoconv[0:4]), int(_dtoconv[5:7]), int(_dtoconv[-2:]))


def main():
    #El número ID debe contener solamente 4 digitos, estos 4 digitos pueden contener números del 0-9
    askandcheck("^[0-9]{4}$", "ID (4 dígitos): ")
    numeroID=captura
    #El nombre que nos da el usuario puede contener de 1-20 letras.
    askandcheck("^([A-Z ]){1,20}$", "Nombre: ")
    nombre=captura
    #Si acepta tiene dos opciones para responder S o N
    askandcheck("^[S|N]$", "Acepta (S/N): ")
    acepta=captura
    #Coloca las cosas que debe tener la fecha, y realiza la pregunta, de lo contrario marcara error.
    askandcheck("^(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])$", "Dame una fecha (YYYY-MM-DD): ")
    fecha=captura

    #Impresión de las variables anteriores
    print(numeroID)
    print(nombre)
    print(acepta)
    print(fecha)