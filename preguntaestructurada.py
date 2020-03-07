#Se usa para la validación de expresiones regulares
import re
#Esta funcion se usa para poder trabajar con datos tipo datetime
import datetime

def askandcheck(_ask,_type="int",_check="^([+-]?[1-9]\d*|0)$"):
    _captura=""
    #Lo que se va hacer ahora es realizar el procedimiento de distintas preguntas con distintos tipos de datos.
    #Lo que esta entre parentesis en cada cambio de tipo de dato, es la variable con la que esta trabajando en ese momento.
    #Procedimiento para int (edad)
    if _type=="int":
        while True:
            _captura=input(_ask)
            if re.search(_check,_captura):
                return int(_captura)
                break
            else:
                print("El dato no tiene el tipo correcto")
                
    #Procedimiento para float (dinero)
    if _type=="float":
        _check="^[-+]?\d*\.?\d*$"
        while True:
            _captura=input(_ask)
            if re.search(_check,_captura):
                return float(_captura)
                break
            else:
                print("El dato no tiene el tipo correcto")
                
    #Procedimiento para date (fechanacimiento)
    if _type=="date":
        _check="^[0-9]{4}/[0-9]{2}/[0-9]{2}$"
        while True:
            _captura=input(_ask)
            if re.search(_check,_captura):
                    try:
                        anio=int(_captura[0:4])
                        mes=int(_captura[5:7])
                        dia=int(_captura[-2:])
                        return datetime.date(anio,mes,dia)
                    except ValueError:
                        print("El dato no es una fecha calendario correcta")
            else:
                print("El dato no tiene formato correcto AAAA/MM/DD")
                
    #Procedimiento para email (correo)
    if _type=="email":
        _check="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        while True:
            _captura=input(_ask)
            if re.search(_check,_captura):
                return _captura
                break
            else:
                print("El dato no tiene formato de correo")
                
    # Procedimiento para email (personal)
    if _type=="custom":
        _check=_check
        while True:
            _captura=input(_ask)
            if re.search(_check,_captura):
                return _captura
                break
            else:
                print("El dato no tiene formato de correo")

#Por último se imprime
def main():
    personal=askandcheck("Dame tu RFC:","custom","^[A-Z]{3,4}-[0-9]{6}-[A-Z0-9]{3}")
    print(personal)
    print(type(personal))

    correo=askandcheck("Dame tu correo:","email")
    print(correo)
    print(type(correo))

    edad=askandcheck("Dame tu edad:")
    print(edad)
    print(type(edad))

    dinero=askandcheck("Cuánto dinero tienes:","float")
    print(dinero)
    print(type(dinero))

    fechanacimiento=askandcheck("Qué fecha naciste:","date")
    print(fechanacimiento)
    print(type(fechanacimiento))
