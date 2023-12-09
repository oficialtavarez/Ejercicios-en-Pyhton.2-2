class CuentaBancaria:

    def __init__(self, numero_de_cuenta, titular, saldo):
        self.numero_de_cuenta = numero_de_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        self.saldo -= cantidad

    def calcular_interes(self, tasa_de_interes):
        self.saldo += self.saldo * tasa_de_interes

    def ingresar(self):
        print(f"Número de cuenta: {self.numero_de_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")


if __name__ == "__main__":
    cuenta = CuentaBancaria(12345678, "Jeremi santos", 2000)
    cuenta.depositar(500)
    cuenta.retirar(200)
    cuenta.calcular_interes(0.05)
    cuenta.ingresar()

