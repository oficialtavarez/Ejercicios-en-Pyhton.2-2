#Código:

class alumno:
   nombre="Anderson"
   apellido="Tavarez"

#Código:

class Alumno:
    nombre = ""
    apellido = ""
  
    def NombreCompleto(self):
        return self.nombre + " " + self.apellido

alu = Alumno()
alu.nombre = input("Nombre...: ")
alu.apellido = input("Apellido...: ")

print(alu.NombreCompleto())

#Código:

class Alumno:
   
       def NombreCompleto(self,nombre,apellido):
        return nombre + " " + apellido

alu = Alumno()
alu.nombre = input("Nombre...: ")
alu.apellido = input("Apellido...: ")

print(alu.NombreCompleto(nombre,apellido))


#Código:

class Alumno:
   
       def NombreCompleto(self,nombre,apellido):
        return nombre + " " + apellido

alu = Alumno()
alu.nombre = input("Nombre...: ")
alu.apellido = input("Apellido...: ")

print(alu.NombreCompleto(nombre,apellido))

#Código: 

Cajero Automático:
#Clases
class CajeroAutomatico:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return f"Gracias Anderson. Su saldo de rico es: {self.saldo}"
        else:
            return "Error: eres pobre."

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            return f"Retiro millonario. Su saldo de rico es: {self.saldo}"
        else:
            return "Error: Eres pobre."

cajero = CajeroAutomatico(1000800)

print(f"Saldo actual: {cajero.consultar_saldo()}")
print(cajero.depositar(500))
print(f"Saldo actual: {cajero.consultar_saldo()}")
print(cajero.retirar(200))
print(f"Saldo actual: {cajero.consultar_saldo()}")

#codigo
class Alumno:
nombre =""
apellido=""
def NombreCompleto(self):
return self.nombre + " " + self.apellido
alu = Alumno()
alu.nombre = input("Nombre..:")
alu.apellido = input("Apellido..:")
print(alu.NombreCompleto())

#codigo: class Alumno:
def NombreCompleto(self, nombre, apellido):
return nombre + " " + apellido
alu = Alumno()
nombre = input("Nombre..:")
apellido = input("Apellido..:")
print(alu.NombreCompleto(nombre,apellido))

#codigo:
n =Nomina()
sueldo = float(input("Entre Sueldo Base :"))
afp = n.Afp(sueldo)
ars = n.Ars(sueldo)
descuentos =n.TotalDesc(afp, ars)
sn = n.SueldoNeto(sueldo,descuentos)
print(" Afp : {:0.2f}".format(afp))
print(" Ars : {:0.2f}".format(ars))
print(" Descuentos : {:0.2f}".format(descuentos))
print(" Sueldo Neto: {:0.2f}".format(sn))