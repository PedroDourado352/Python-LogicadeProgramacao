##Classe é um molde para criar um objeto. Define atributos(caracteristicas) e metodos (ações)

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

meu_carro = Carro("Toyota", "Corolla")
meu_carro.exibir_informacoes()

