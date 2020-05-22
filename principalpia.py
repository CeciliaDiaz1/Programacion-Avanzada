# Se importa la librería para tipo fecha.
import datetime
# Se usa este módulo para poder ejecutar tareas desde el sistema operativo.
import os
#  Se usa este módulo para trabajar con expresiones regulares
import re
# Se pide importar la clase Contacto, que está definida en clasepia.py
from clasepia import Contacto
# Permite extraer elementos de un objeto
from operator import attrgetter
# Permite serializar a JSON
import json

# Lista vacia llamada Contactos
Contactos = []

# Muestra cuales son los elementos en la lista.
def CuantosContactossHay():
    txt = "El número de elementos de la colección es {}"
    print(txt.format(len(Contactos)))

# Se define para recaudar los datos del contacto, dentro del menú.
def IngresoDatos():
    askandcheck("^([A-Z ]){1,15}$", "Ingresa el Nickname: ")
    nick=captura
    askandcheck("^([A-Z ]){1,35}$", "Ingresa el Nombre: ")
    nombre=captura
    askandcheck('\w+@\w+', "Inserta tu correo: ")
    correo=captura
    askandcheck('^("^[0-9]{10}$", "¿Ingresa el telefono (99 9999-9999): ")
    telefono=captura
    askandcheck("^(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])$", "Dame una fecha (YYYY-MM-DD): ")
    fechanacimiento=captura
    askandcheck("^([0-9]){1,7}$", "Ingresa los gastos por mes: ")
    gastos=captura
    Contactos.append(Contacto(nick,nombre,correo,telefono,fechanacimiento,gastos))

#Esto es para agregar contactos de manera manual.
Contactos.append(Contacto(str("master1"),str("Cecilia Díaz"), str("ceci.g@hotmail.com"), int(8128391278), (datetime.datetime(2020, 5, 17), int(3,500)))
CuantosContactosHay()

# Esta función se usa para borrar pantalla.
LimpiarPantalla = lambda: os.system('cls') #on Windows System

# Se usa para validar expresiones regulares
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

#Opciones del menú
def principal():
    while (True):
        LimpiarPantalla()
        print("LISTA DE COTACTOS")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
        #Pregunta para saber que opción desea realizar el usuario
        opcion_elegida = input("¿Qué quieres hacer?  > ")
        # Lo que hace esta linea es validar que el dato que se introduzca cumpla con
        # ciertos requisitos.
        if RegEx(opcion_elegida,"^[123450]{1}$"):
            if opcion_elegida=="0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
            # Si se escoge la opción 1 se hace realiza lo siguiente.
            if opcion_elegida=="1":
                print IngresoDatos()
            # Si se escoge la opción 2 se hace realiza lo siguiente.
            if opcion_elegida=="2":
            datoValido=False
            while True:
                contacto_buscar = int ("¿Que contacto deseas buscar? (dime su numero porfavor) ")
                    if RegEx(contacto_eliminar,"^[0-9]{10}$"):
                    if contacto_buscar in Contactos:
                        datoValido=True
                        break
                     else:
                        print("Se requiere nombre, apellido, no mayor a 30 catacteres.")
                        datoValido=False
                        entidadValida=(entidadValida & datoValido)
            # Si se escoge la opción 3 se hace realiza lo siguiente.
            if opcion_elegida=="3":
                contacto_eliminar = int ("¿Que contacto deseas eliminar? (dime su numero porfavor) ")
                if RegEx(contacto_eliminar,"^[0-9]{10}$"):
                Contactos.pop (contacto_eliminar)
                print("El contacto se elimino")
            # Si se escoge la opción 4 se hace realiza lo siguiente.
            if opcion_elegida=="4":
                print (Contactos)
            # Si se escoge la opción 5 se hace realiza lo siguiente.
            if opcion_elegida=="5":
                print (Contactos)
                json_data = json.dumps(Contactos, default=lambda o: o.__dict__, indent=4)
                print(json_data)
            # Esta linea es para que posteriormente se cierre el ciclo.
            input("Pulsa enter para contunuar...")
            break
        else:
            #Estas dos lineas se usan en caso de que el dato ingresado sea incorrecto.
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")
principal()
