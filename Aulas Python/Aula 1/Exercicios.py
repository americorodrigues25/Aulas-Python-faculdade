#----------------EXERCICIO 1-------------------#
peso = float (input("Digite seu peso: "))
altura = float (input("Digite sua altura: "))
calcIMC = peso / (altura*altura)

if (calcIMC <18.5):
    print("Você está abaixo do peso !")

elif (calcIMC >=18.5 and calcIMC <=24.9):
    print("Seu peso é o ideal !")

elif (calcIMC >=25 and calcIMC<=29.9):
    print("Você está acima do peso !")

elif (calcIMC >=30 and calcIMC<=39.9):
    print("Você está obeso !")

else:
    print("Seu grau de obesidade é muito grave !")

print("Seu IMC é: ", calcIMC)

#----------------EXERCICIO 2-------------------#

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digte a nota 3: "))
media = (n1+n2+n3) / 3

print ("Aluno, sua média é: ", media)





