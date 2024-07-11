class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

class Caminhao(Veiculo):
    def __init__(self, modelo, ano, eixo):
        super().__init__(modelo, ano)
        self.eixo = eixo

    def ExibirTipoEixo(self):
        if self.eixo == 1:
            return "Capacidade até 6 toneladas"
        
        elif self.eixo == 2:
            return "Capacidade até 13 toneladas"
        
        elif self.eixo == 3:
            return "Capacidade até 30 toneladas"
        
        else:
            "Numero invalido"

modelo = input("Digite o modelo do caminhão: ")
ano = input("Digite o ano do caminhão: ")
eixo = int(input("Digite a quantidade de eixos do caminhão (1, 2 ou 3): "))

caminhao = Caminhao(modelo, ano, eixo)
print ("Quantidade de eixos: ", caminhao.ExibirTipoEixo())


