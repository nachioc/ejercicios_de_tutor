"""

Crear una clase para trabajar con una Persona.

Agregarle 3 atributos de instancia, 

por lo menos 2 de clase, el constructor y dos métodos 

(uno con parámetros y otro sin parámetro). 

Luego instanciar a dos personas. 

"""

class Persona:

  ser_vivo = True # atributos de clase

  poblacion = 0

  def __init__(self, nombre, año_nacimiento, telefono=None):

    self.nombre = nombre.upper() # atributo de instancia

    self.nacimiento = año_nacimiento # atributo de instancia

    self.telefono = telefono # atributo de instancia

    Persona.poblacion += 1 # modifica atributo de clase cada vez que se crea un objeto

  def obtener_datos(self):

    return (f"Nombre 🙂: {self.nombre} \n"

        f"Teléfono 🤳: {self.telefono} \n"

        f"Año de nacimiento 🐣: {self.nacimiento}")

  def obtener_edad(self, año):

    """Tienes que ingresar el año actual"""

    edad = año - self.nacimiento

    return f"{self.nombre} tiene {edad} años de edad."

persona_1 = Persona(nombre="beethoven", año_nacimiento=2000) # argumentos por nombre

print(persona_1.obtener_datos())

print(persona_1.obtener_edad(año=2022))

print(f"{persona_1.ser_vivo=}")

print(f"{Persona.poblacion=}")

print("*" * 50)

persona_2 = Persona("aristóteles", 1000, telefono="beta123") # argumentos por posición

print(persona_2.obtener_datos())

print(persona_2.obtener_edad(2022))

print(f"{persona_2.ser_vivo=}")

print(f"{Persona.poblacion=}")