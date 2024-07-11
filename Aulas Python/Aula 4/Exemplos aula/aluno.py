from pessoa import *
class Aluno(Pessoa):
    def __init__(self, nome, snome, email, tel, N_Matricula):
        super().__init__(nome, snome, email, tel, N_matricula=N_Matricula)
        self.N_Matricula = N_Matricula
    
    def ExibirMatricula(self):
        return "Matrícula do aluno: " + self.N_Matricula

aluno1 = Aluno("Américo", "Rodrigues", "americo@gmail.com", "11 96416-6962", "2265-17-2")
print(aluno1.ExibirMatricula())

