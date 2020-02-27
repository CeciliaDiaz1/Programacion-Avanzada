# Cuando una variable es declarada fuera del código es global
variableglobal="Soy global"
#Si dentro del codigo se quiere usar funcion global se debe anteponer la "variableglobal"

def pendiente():
    pass

def norecibeargumentos():
    variableglobal=4
    print("No recibe argumentos")
    print(variableglobal)

def recibeargumentos(fname, lname):
#Los argumentos dentro de este parentesis se desarrollaran en forma de lista con una separación de ""
    print(fname + " " + lname)
    print(variableglobal)

#Si se le asigna un valor a un argumento este sera opcional
def argumentosopcionales(city, country = "Mexico"):
    print("I am from " + city + ", " + country)

#Esta funcion retorna valores
def elevoalcuadrado(x):
  return x * x

def main():
    print(elevoalcuadrado(4))