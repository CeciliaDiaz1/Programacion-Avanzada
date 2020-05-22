# Se importa la librería para tipo fecha.
import datetime

# Se define la clase Contacto.
class Contacto:

# Propiedades de la clase.
  def __init__(self, nickname, nombre,correo,telefono,fechanacimiento,gastos):
    # nickname = Nombre a traves del cual el contacto desea ser referido
    self.nickname=nickname
    # nombre = Nombre completo del usuario.
    self.nombre=nombre
    # correo = Correo del contacto.
    self.correo=correo
    # telefono = Tlefono del contacto.
    self.telefono= telefono
    #fechanacimiento = Fecha de nacimiento del contacto
    self.fechanacimiento=fechanacimiento
    #gastos = Gasto mensual del contacto
    self.gastos=gastos
    
