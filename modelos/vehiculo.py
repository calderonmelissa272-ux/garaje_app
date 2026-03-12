class Vehiculo:
    def __init__(self, placa, marca, modelo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo}"
