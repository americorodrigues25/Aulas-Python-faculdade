class Aluno:
    def __init__(self, nome, n1, n2):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.__mediafinal = 7

    @property
    def mediafinal(self):
        return self.__mediafinal
    
    @mediafinal.setter
    def mediafinal(self, novamedia):
        raise ValueError("Impossivel calcular a média !")
    
    def calcular_media(self):
        self.__mediafinal (self.n1 + self.n2) / 2

aluno = Aluno('Américo', 9, 9)
aluno.mediafinal = 100
print(aluno.nome)
print(aluno.mediafinal)