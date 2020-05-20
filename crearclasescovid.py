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
    def __init__(self,Pais,Fecha,NContangios,NFallecidos):
        self.Fecha = Fecha
        self.Pais = Pais
        self.NContangios = NContangios
        self.NFallecidos = NFallecidos

