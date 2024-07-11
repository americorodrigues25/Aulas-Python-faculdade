class Cliente:
    def __init__(self, codigo, endereco):
        self.codigo = codigo
        self.endereco = endereco

    def Exibir_end(self):
        return "Endereço: " + self.endereco

end = Cliente("01", "Rua Odilon de Souza - 200 - Suzano")
print (end.Exibir_end())

class Cliente_fisico(Cliente):
    def __init__(self, codigo, endereco, nome, CPF):
        super().__init__(codigo, endereco)
        self.CPF = CPF
        self.nome = nome

    def Verificar_CPF(self):
        return "CPF: " + self.CPF
    
cpf = Cliente_fisico("01", "Rua Odilon de Souza - 200 - Suzano", "Macario", "481.778.208-13")
print (cpf.Verificar_CPF())

class Cliente_jurico(Cliente):
    def __init__(self, codigo, endereco, CNPJ, razao_social):
        super(). __init__(codigo, endereco)
        self.CNPJ = CNPJ
        self.razao_social = razao_social

    def Verificar_CNPJ(self):
        return "CNPJ: " + self.CNPJ + self.razao_social
    
cnpj = Cliente_jurico("01", "Rua Odilon de Souza - 200 - Suzano", "123456/0001-43", "\nAmérico Eireli - ME")
print (cnpj.Verificar_CNPJ())
            
