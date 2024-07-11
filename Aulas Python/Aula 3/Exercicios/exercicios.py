def notas(nota1,nota2):
    return (nota1 + nota2) / 2

nota1=int (input("Digite a primeira nota: "))
nota2=int (input("Digite a segunda nota: "))

soma=notas(nota1,nota2)

print("Media: " , soma)

#------------------------------------------------------#

def valor(horaaula,horatrabalho):
    return (horaaula*horatrabalho)

horaaula=float(input("Digite o valor da sua hora aula: "))
horatrabalho=float(input("Digite a quantidade de horas trabalhadas: "))

soma=valor(horaaula,horatrabalho)

print("Seu salario é: ",soma)

#------------------------------------------------------#

def invertevalor(valor):
    valorstr=str(valor)
    valorinvertido=valorstr[::-1]
    return int(valorinvertido)

numero=int(input("Digite um numero: "))
print (invertevalor(numero))

#str é usada para transformar numero em texto
#------------------------------------------------------#

def digitos(numero):
    return len(str(numero))

valor =int(input("Digite um valor: "))
print (digitos(valor))


