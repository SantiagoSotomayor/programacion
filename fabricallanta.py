#Crear una clase fabrica que tenga los atributos dde llantas, color y precio, luego crear dos clases
# las cuales son Moto y Carro.
#por ultimo, crear objetos para cada clase y mostrar por pantalla cada atributos
class Fabrica:
    def _init_(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

class Moto(Fabrica):
    def _init_(self, llantas, color, precio, cilindrada):
        super()._init_(llantas, color, precio)
        self.cilindrada = cilindrada

class Carro(Fabrica):
    def _init_(self, llantas, color, precio, puertas):
        super()._init_(llantas, color, precio)
        self.puertas = puertas

        Moto = Moto(2, "rojo", 5000, 250)
print(Moto. llantas)  # 2
print(Moto.color)  # rojo
print(Moto.precio)  # 5000
print(Moto.cilindrada)  # 250

carro = Carro(4, "azul", 15000, 4)
print(carro.llantas)  # 4
print(carro.color)  # azul
print(carro.precio)  # 15000
print(carro.puertas)  # 4