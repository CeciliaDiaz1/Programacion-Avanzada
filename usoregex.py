#Se importa la función "re"; requerido para usar expresiones regulares.
import re

def main():
  while True:
    #Esta linea pregunta el dato que se desea conocer.
    strRFC = input("Dame el RFC: ")
    #Si el RFC que nos da el usuario "coincide" con los terminos con los que debe contar un RFC
    coincide = re.search("^[A-Z]{4}-[0-9]{6}-[A-Z0-9]{3}$", strRFC)
    if (coincide):
      #Se imprimira que el RFC que nos dio es correcto
      print("RFC Correcto!")
      #Y se terminara el programa con la funcion "break"
      break
      #Si no
    else:
      #Se seguira repitiendo, y nos imprimira el siguente mensaje, hasta que el RFC sea el correcto.

      #De lo contrario el codigo sera infinito y no se detendra
      print("RFC incorrecto. Intenta de nuevo.")