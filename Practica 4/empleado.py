class Empleado:
    def __init__(self, nombre='', apellidos='', edad=0, sexo='', direccion='', email='', sueldo=0.0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
        self.email = email
        self.sueldo = sueldo

    def asignar_sueldo(self, sueldo):
        self.sueldo = sueldo

    def calcular_AFP(self):
       
        return self.sueldo * 0.0287

    def calcular_SFS(self):
     
        return self.sueldo * 0.0304

    def calcular_ISR(self):      
        if self.sueldo <= 416220.00:
            return 0
        elif self.sueldo <= 624329.00:
            return (self.sueldo - 416220.01) * 0.15
        elif self.sueldo <= 867123.00:
            return 31216.00 + (self.sueldo - 624329.01) * 0.20
        else:
            return 79776.00 + (self.sueldo - 867123.01) * 0.25

    def imprimir_informacion(self):
        return f'Nombre: {self.nombre}\nApellidos: {self.apellidos}\nEdad: {self.edad}\nSexo: {self.sexo}\nDirección: {self.direccion}\nEmail: {self.email}\nSueldo: {self.sueldo}'
