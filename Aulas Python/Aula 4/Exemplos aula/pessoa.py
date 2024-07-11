class Pessoa:
    def __init__(self, nome, snome, email, tel, N_matricula):
        self.nome=nome
        self.snome=snome
        self.email=email
        self.tel=tel

    def ExibirNome_Completo(self):
        return "Nome completo: " + self.nome + " " + self.snome 
    
    def ExibirTel(self):
        return "Numero de telefone: " + self.tel
    
    def ExibirEmail(self):
        return "E-mail: " + self.email

pessoa=Pessoa("Américo", "Rodrigues", "americo@gmail.com", "11 96416-6962", "2265-17-2")
print(pessoa.ExibirNome_Completo())
print(pessoa.ExibirEmail())
print(pessoa.ExibirTel())
