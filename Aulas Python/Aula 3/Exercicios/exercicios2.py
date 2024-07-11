#               QUESTÕES                #

#Questão 1 = Resposta b / Questão 2 = Resposta b#    


#----------------EXERCICIO 1------------------#
def nome_idade (nome,idade):
    return (nome,idade)
nome=(input("Digite seu nome: "))
idade=int (input("Digite sua idade: "))

if (idade >18):
    print("Bem vindo(a)! ", nome,", Você é maior de idade !")

else:
    print ("Bem vido(a)! ",nome,", Você é menor de idade")

#----------------EXERCICIO 2------------------#
    
def IMC (peso,altura):
    return peso / (altura*altura) 
nome=(input("Digite seu nome: "))
peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
IMC= peso / (altura*altura)
print (nome, "Seu IMC é: ",IMC)

#----------------EXERCICIO 3------------------#

def senhavalida(senha):
    senha=str(senha)
    numeroscaracteres = False
    temMaiusculo = False
    temMinusculo = False

    if(numeroscaracteres <8):
        print("Senha invalida, digite uma senha com letras maiusculas, minusculas e numeros.")
        return
    for caracteres in senha:
        if(caracteres.isupper()):

            temMaiusculo = True
        elif(not caracteres.islower()):
            temMinusculo = True

        if(temMaiusculo ==False):
            print("Senha valida, porém fraca, refaça com maiusculas!", senha)
            return
        if (temMinusculo ==False):
            print("Senha valida, porém fraca, refaça com minusculas", senha)
            return
        print("Senha valida", senha)
senhavalida(input("Digite sua senha: "))

#----------------------------------------------------------------------------#

def verificarsenha(senha):
    digitos=len(senha)
    if(digitos>=8):
        return "Senha invalida !"
    else:
        return "Senha invalida ! Tente novamente."
senha=(input("Digite sua senha: "))
print (verificarsenha(senha))