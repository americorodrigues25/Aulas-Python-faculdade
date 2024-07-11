from exercicio import *
class Professor(Pessoa):
    def __init__(self, nome, snome, email, tel, salario):
        super().__init__(nome, snome,email, tel)
        self.salario=salario
    
    def ExibirTipoSalario(self, salario):
        if salario >4000:
            return "Você está acima da média"
        else:
            return "Você está abaixo da média"
        
prof1=Professor("Maria", "Santos", "maria@gmail.com", "11 99999-9999", 5000)
print(prof1.ExibirNome_Completo())
print(prof1.ExibirTipoSalario(prof1.salario))