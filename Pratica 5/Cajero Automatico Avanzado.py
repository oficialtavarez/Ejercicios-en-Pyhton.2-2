#Hola, los datos de usuario son los siguientes: Cuenta: 987654321  Clave:9684 debe colocarlos para poder usar el cajero.
#pues se creo para eso.

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre

class Cuenta:
    def __init__(self, numero_cuenta, saldo, limite_credito, tipo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.limite_credito = limite_credito
        self.tipo_cuenta = tipo_cuenta

class Cliente:
    def __init__(self, nombre, direccion, numero_cuenta, saldo_inicial):  
        self.nombre = nombre
        self.direccion = direccion
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial  

class Cajero:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

class CajeroAutomatico:
    def __init__(self, banco, clientes):
        self.banco = banco
        self.clientes = clientes

    def validar_usuario(self, numero_cuenta, contraseña):
        for cliente in self.clientes:
            if cliente.numero_cuenta == numero_cuenta and contraseña == "9684":  
                return True
        return False

    def retirar_efectivo(self, numero_cuenta, contraseña, cantidad):
        for cliente in self.clientes:
            if cliente.numero_cuenta == numero_cuenta and contraseña == "9684": 
                if cantidad <= cliente.saldo:
                    cliente.saldo -= cantidad
                    print(f"Retirada exitosa. Nuevo saldo: {cliente.saldo}")
                else:
                    print("Saldo insuficiente para esta operación.")

    def ingresar_efectivo(self, numero_cuenta, contraseña, cantidad):
        for cliente in self.clientes:
            if cliente.numero_cuenta == numero_cuenta and contraseña == "9684":  
                cliente.saldo += cantidad
                print(f"Ingreso de efectivo exitoso. Nuevo saldo: {cliente.saldo}")

    def pagar_factura(self, numero_cuenta, contraseña, info_factura):
        for cliente in self.clientes:
            if cliente.numero_cuenta == numero_cuenta and contraseña == "9684":  
                print(f"Factura pagada: {info_factura}")

    def transferir_fondos(self, numero_cuenta, contraseña, info_cuenta_destino, cantidad):
        for cliente in self.clientes:
            if cliente.numero_cuenta == numero_cuenta and contraseña == "9684":  
                if cantidad <= cliente.saldo:
                    cliente.saldo -= cantidad
                    print(f"Transferencia exitosa. Nuevo saldo: {cliente.saldo}")
                else:
                    print("Saldo insuficiente para esta transferencia.")

# Usuarios
cliente1 = Cliente("Juan", "Calle Principal 123", "123456789", 5000)
cliente2 = Cliente("Anderson", "Avenida Central 456", "987654321", 3000)

# Uso del cajero automático
banco_principal = Banco("Banco Principal")
clientes = [cliente1, cliente2]

cajero_principal = Cajero("Cajero Principal", "1234")
cajero_automatico = CajeroAutomatico(banco_principal, clientes)

# Solicitud
numero_cuenta = input("Ingrese el número de cuenta: ")
contraseña = input("Ingrese la contraseña: ")
u
# Validar 
if cajero_automatico.validar_usuario(numero_cuenta, contraseña):
    print("Usuario autenticado como Anderson.")
    # Solicitar 
    print("¿Qué desea hacer?")
    print("1. Retirar efectivo")
    print("2. Ingresar efectivo")
    print("3. Pagar factura")
    print("4. Transferir fondos")
    
    opcion = int(input("Ingrese el número de la operación que desea realizar: "))

    if opcion == 1:
        cantidad = float(input("Ingrese la cantidad que desea retirar: "))
        cajero_automatico.retirar_efectivo(numero_cuenta, contraseña, cantidad)
    elif opcion == 2:
        cantidad = float(input("Ingrese la cantidad que desea ingresar: "))
        cajero_automatico.ingresar_efectivo(numero_cuenta, contraseña, cantidad)
    elif opcion == 3:
        info_factura = input("Ingrese la información de la factura: ")
        cajero_automatico.pagar_factura(numero_cuenta, contraseña, info_factura)
    elif opcion == 4:
        info_cuenta_destino = input("Ingrese la información de la cuenta destino: ")
        cantidad = float(input("Ingrese la cantidad que desea transferir: "))
        cajero_automatico.transferir_fondos(numero_cuenta, contraseña, info_cuenta_destino, cantidad)
    else:
        print("Opción no válida.")
else:
    print("Usuario o contraseña incorrectos.")
