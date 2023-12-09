class Estudiante:

    def __init__(self, nombre, apellidos, edad, sexo, direccion, carrera, email, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
        self.carrera = carrera
        self.email = email
        self.telefono = telefono

    def ingresar_informacion(self):
        self.nombre = input("Ingrese el nombre del estudiante: ")
        self.apellidos = input("Ingrese los apellidos del estudiante: ")
        self.edad = int(input("Ingrese la edad del estudiante: "))
        self.sexo = input("Ingrese el sexo del estudiante (M/F): ")
        self.direccion = input("Ingrese la dirección del estudiante: ")
        self.carrera = input("Ingrese la carrera del estudiante: ")
        self.email = input("Ingrese el email del estudiante: ")
        self.telefono = int(input("Ingrese el teléfono del estudiante: "))

    def imprimir_informacion(self):
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)
        print("Dirección:", self.direccion)
        print("Carrera:", self.carrera)
        print("Email:", self.email)
        print("Teléfono:", self.telefono)

    def instanciar(self):
        estudiante = Estudiante("Jeremi", "Santos", 22, "M", "Punta rusia", "Ingeniería Informática", "jeremis103@gmail.com", 8492780438)
        estudiante.ingresar_informacion()
        estudiante.imprimir_informacion()


if __name__ == "__main__":
    estudiante = Estudiante("Jeremi", "Santos", 22, "M", "Calle 123", "Ingeniería Informática", "jeremis103@gmail.com", 9492780438)
    estudiante.ingresar_informacion()
    estudiante.imprimir_informacion()