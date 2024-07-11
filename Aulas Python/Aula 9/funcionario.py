class Funcionario:

    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def mostrardados(self):
        return "Nome: " + self.nome + " "+"Salário: "+ str(self.salario)
    
    def receber_bonificacao(self):
        return self.salario * 0.5
    
class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self.qtd_funcionarios = qtd_funcionarios

    def receber_bonificacao(self):
        return super().receber_bonificacao() + 300
    
class Estagiario(Funcionario):

    def __init__(self, nome, cpf, salario, setor):
        super().__init__(nome, cpf, salario)
        self.setor = setor

    def receber_bonificacao(self):
        return super().receber_bonificacao() + 180

    
gerente = Gerente('José', '2222222222-2', 5000.0, '1234', 0)
funcionario1 = Funcionario('maria', '46146164164', 5000)
print(funcionario1.mostrardados())
print(funcionario1.receber_bonificacao())

funcionario = Funcionario('Marcos', '213131313131', 5000.0)
print(funcionario.mostrardados())
print(funcionario.receber_bonificacao())

gerente = Gerente('José', '2222222222-2', 5000.0, '1234', 0)
print(gerente.mostrardados())
print(gerente.receber_bonificacao())
        

estagiario = Estagiario('Américo', '431.778.208-13', 15000.0, 'Estagiário')
print(estagiario.mostrardados())
print(estagiario.receber_bonificacao())

