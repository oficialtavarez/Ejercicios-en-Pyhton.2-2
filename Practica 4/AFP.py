class Persona:
    def __init__(self, nombre="", apellidos="", edad=0, sexo="", direccion="", email="", sueldo=0.0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
        self.email = email
        self.sueldo = sueldo

    def asignar_sueldo(self, nuevo_sueldo):
        self.sueldo = nuevo_sueldo

    def calcular_afp(self):
        afp_descuento = 0.0725
        return self.sueldo * afp_descuento

    def calcular_sfs(self):
        sfs_descuento = 0.03
        return self.sueldo * sfs_descuento

    def calcular_irs(self):
        irs_descuento = 0.15
        return self.sueldo * irs_descuento

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Dirección: {self.direccion}")
        print(f"Email: {self.email}")
        print(f"Sueldo: {self.sueldo}")
        print(f"Descuento AFP: {self.calcular_afp()}")
        print(f"Descuento SFS: {self.calcular_sfs()}")
        print(f"Descuento IRS: {self.calcular_irs()}")
