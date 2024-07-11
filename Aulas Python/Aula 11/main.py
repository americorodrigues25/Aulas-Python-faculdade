class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhda):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhda
        self.__horas_trabalhadas = 160
        self.__salario = 0

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("Impossivel alterar salario diretamente. Use a função calcula_salario().")

    def registra_hora_trabalhada(self):
        self.valor_hora_trabalhada +=1
    
    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada
    
funcionario1 = Funcionario('Américo', 'Dev Front-End', 250)
funcionario1.salario = 10000
print(funcionario1.nome)
print(funcionario1.cargo)
print(funcionario1.salario)