class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def calcula_salario(self):
        pass

class Contrato_Carteira(Funcionario):
    def __init__(self, nome, qtda_horas, valor_hora):
        super().__init__(nome)
        self.qtda_horas = qtda_horas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.qtda_horas * self.valor_hora
    
class Comissionado_Temporario(Funcionario):
    def __init__(self, nome, total_vendas):
        super().__init__(nome)
        self.total_vendas = total_vendas

    def calcular_salario(self):
        return self.total_vendas * 0.1
    
carteira = Contrato_Carteira('nome', 360, 150)
print(carteira.calcular_salario())

comissionado = Comissionado_Temporario('nome', 500)
print(comissionado.calcular_salario())