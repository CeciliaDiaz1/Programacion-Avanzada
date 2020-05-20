import datetime
#Implementación de datos de tipo fecha

# Nombre de la clase
class Pais():

#Esta clase tiene 5 propiedades, mismas que estan entre parentesis (argumentos)
# Argumentos  
    def __init__(self,NombreIng,NombreEsp,Fallecidos,Contagiados, PDC):


#Objetos
        self.NombreIng = NombreIng
        #NombreIng = Nombre del pais en ingles (str)
        self.NombreEsp = NombreEsp
        #NombreEsp = Nombre del pais en español (str)
        self.Fallecidos = Fallecidos
        #Fallecidos = Total de fallecidos en el pais (int)
        self.Contagiados = Contagiados
        #Contagiados = Total de contagiados en el pais (int)
        self.PDC = PDC
        #PDC = Primer dia contagio (datetime)

class  Incidente():
    def __init__(self,Fecha,Pais,NContangios,NFallecidos):
        self.Fecha = Fecha
        self.Pais = Pais
        self.NContangios = NContangios
        self.NFallecidos = NFallecidos

#Instanciar la clase Pais (se crea un objeto de la clase)
mipais = Pais (str("Mexico"),str("México"), int (1000), int (5000), datetime.datetime(2020, 5, 18))
print (mipais.PDC)

#Instanciar la clase siguiente Incidente
incidenteAyer = Incidente (datetime.datetime(2020, 5, 17), str ("México"), int(1500), int(18))
incidenteHoy = Incidente (datetime.datetime.now() , str ("México"), int(1400), int(12))

#Crear una lista
mi_lista = []

#Agregar elementos a la lista
#El append se utiliza para agregar obejos a una lista.
mi_lista.append(incidenteAyer)
mi_lista.append(incidenteHoy)

#Contar cuantos registros tenemos ahora en la lista
print(len(mi_lista))

for elemento in mi_lista:
    print (elemento.Fecha)

#INSTANCIAR 5 PAISES A UNA LISTA LLAMADA (mis_paises)

#Crear una lista para instanciar 5 paises
mis_paises = []

#Instanciar/Agregar 5 paises a la clase Pais
pais1 = Pais (str("Colombia"),str("Colombia"), int (800), int (4200), datetime.datetime(2020, 4, 20))
pais2 = Pais (str("Germany"),str("Alemania"), int (1600), int (6400), datetime.datetime(2020, 4, 3))
pais3 = Pais (str("Peru"),str("Perú"), int (500), int (2900), datetime.datetime(2020, 5, 1))
pais4 = Pais (str("China"),str("China"), int (10000), int (80000), datetime.datetime(2020, 2, 4))
pais5 = Pais (str("Italy"),str("Italia"), int (3500), int (12000), datetime.datetime(2020, 3, 9))

#Agregamos los elementos a la lista creada (mis_paises)
mis_paises.append(pais1)
mis_paises.append(pais2)
mis_paises.append(pais3)
mis_paises.append(pais4)
mis_paises.append(pais5)

#Contar cuantos registros tenemos ahora en la lista
print(len(mis_paises))