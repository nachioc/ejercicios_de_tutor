"""

Crear una clase Atleta, que tenga su nombre, 

apellido, altura, peso, teléfono 

e índice de masa corporal (descripción). 

Decidir qué atributos deben ser públicos 

y cuáles privados. Crear los métodos get 

y set que crea necesarios. 

Forumula IMC = Peso / (altura x altura)

"""

class Atleta:

  def __init__(self, nombre, apellido, altura, peso, telefono=None):

    self.nombre = nombre

    self.apellido = apellido

    self.__altura = altura

    self.__peso = peso

    self.telefono = telefono

    self.imc = self.calcular_imc()

  def __str__(self):

    return f"El atleta '{self.apellido.upper()}, {self.nombre}' tiene un IMC = {self.imc:.2f}"

  def get_peso(self):

    return self.__peso

  def set_peso(self, nuevo_peso):

    self.__peso = nuevo_peso

  def calcular_imc(self):

    if self.__peso > 0 and self.__altura > 0:

      self.imc = self.__peso / self.__altura**2

      return self.imc

a1 = Atleta("Usain", "Bolt", 1.95, 89)

a2 = Atleta("Esteban", "Acevedo", 1.80, 73)

print(a1)

print(a2)