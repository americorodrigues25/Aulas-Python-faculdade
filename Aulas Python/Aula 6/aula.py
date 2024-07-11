class Veiculo:
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def Exibir_Chassi(self):
        return "Chassi: " + self.chassi
    
    def Exibir_ano_marca_modelo(self):
        return "Ano: " + self.ano + "\nMarca do veiculo: " + self.marca + "\nModelo do veiculo: " + self.modelo
    
v=Veiculo("carro", "123456799", "Gol", "G6", "2017")
print (v.Exibir_Chassi())
print (v.Exibir_ano_marca_modelo())

class Motocicleta(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.cilindrada = cilindrada

    def Exibir_cilindrada(self):
        return "Sua moto tem: " + self.cilindrada + "C"
    
m = Motocicleta("Moto", "13456789", "BMW", "F1200", "2024", "1200")
print (m.Exibir_cilindrada())