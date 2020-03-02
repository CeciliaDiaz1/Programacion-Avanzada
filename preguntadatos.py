#En este código se preguntaran diferentes tipos de datos.
#Esta funcion se usa para poder trabajar con datos tipo datetime
import datetime
# Los datos se tienen, se preguntan o se calculan.

def main():
#En las siguientes lineas se preguntan a el usuario los datos que se desean saber
 strDato = input("Dame un dato string: ")
 _iDato = input("Dame un dato entero: ")
 iDato = int(_iDato)
 _fDato = input("Dame un dato float: ")
 fDato =float(_fDato)
 _dtDato = input("Dame una fecha yyyy/mm/dd: ")
 
 #Aqui lo que se hace es tomar la variable "dtDato" para sacar los datos que se desean, para los cuales se necesita colocar la posicione en la que se encuentra el dato especifico que se require, para que no vuelva a imprimir toda la fecha.

 anio=_dtDato[0:4]
 mes=_dtDato[5:7]
 dia=_dtDato[-2:]
 print(anio)
 print(mes)
 print(dia)

#La siguiente linea lo que hace es encriptar con la función "datetime" las 3 variable, las cuales como se puede ver tienen su tipo de dato por un lado que en este caso es (int; entero)
 dtDato = datetime.datetime(int(anio), int(mes), int(dia))

 print(strDato)
 #Lo que se hace en esta linea es imprimir la variable "strDato"
 print(type(strDato))
 #Y en esta linea se imprimiria el tipo de dato de la variabale. Y asi con las demas variables.
 print(iDato)
 print(type(iDato))
 print(fDato)
 print(type(fDato))
 print(dtDato)
 print(type(dtDato))