class Mascota:
    def __init__(self):
        self.nombre = 'neron'
        self.raza = 'calle'
    def mostrar(self):
        print(f'nombre:{self.nombre}')
        print(f'raza:{self.raza}')
    def leer(self):
        self.nombre = str(input('ingrese una nombre:'))
        self.raza = str(input('ingrese una raza:'))
    def getNombre(self):
        return self.nombre
    def getRaza(self):
        return self.raza
        