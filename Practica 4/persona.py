class Persona:

    def __init__(self, nombre, apellidos, edad, sexo, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion

    def ingresar_informacion(self):
        self.nombre = input("Ingrese el nombre: ")
        self.apellidos = input("Ingrese los apellidos: ")
        self.edad = int(input("Ingrese la edad: "))
        self.sexo = input("Ingrese el sexo: ")
        self.direccion = input("Ingrese la dirección: ")

    def imprimir_informacion(self):
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)
        print("Dirección:", self.direccion)

persona = Persona("Jeremi", "santos", 22, "Hombre", "punta rusia")

persona.ingresar_informacion()

persona.imprimir_informacion()