valor = int (input("Digite um valor: "))
print ("Antecessor: ", valor -1)
print ("Sucessor: ", valor +1)

if valor > 10:
    print ("Valor acima de 10")

#----------------------------------------------------#

valor = int(input("Digite um valor: "))

if valor % 5 == 0:
    print ("Este valor é divisivel por 5\n ",valor )

else:
    print ("Valor não divisivel")


#----------------------------------------------------#


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if ( idade <=9 ):
    print ("Você é criança")

elif (idade >=10 and idade <=17):
    print ("Você é adoslecente")

elif (idade >=18 and idade <=64):
    print ("Você é adulto")

else:
    print("Você é idoso")
