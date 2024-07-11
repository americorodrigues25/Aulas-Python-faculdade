# Contar quantas letras maiúsculas e minúsculas tem numa variável.
def contar_letras(texto):
    maiusculas = 0
    minusculas = 0
    for letra in texto:
        if letra.isupper():
            maiusculas += 1
        elif letra.islower():
            minusculas += 1
    return maiusculas, minusculas

texto = input("Digite um texto: ")
maiusculas, minusculas = contar_letras(texto)

print("Número de letras maiúsculas:", maiusculas)
print("Número de letras minúsculas:", minusculas)

# Saber se o que o usuário digitou é considerada uma senha válida, ou seja, tem maiúsculas, minúsculas, letras, números e caracteres especiais.
def verificar_senha(senha):
    if len(senha) < 8:
        return False
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        else:
            tem_especial = True
    
    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

senha = input("Digite a senha: ")

if verificar_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida!")


# Solicitar o nome, email e CPF do usuário e apresentar o nome em maiúsculas, email em minúsculas e o CPF com os 3 primeiros dígitos em *.
def formatar_cpf(cpf):
    return cpf[:3] + '*'*9

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
cpf = input("Digite seu CPF: ")

nome_formatado = nome.upper()
email_formatado = email.lower()
cpf_formatado = formatar_cpf(cpf)

print("Nome:", nome_formatado)
print("Email:", email_formatado)
print("CPF:", cpf_formatado)


# Solicitar para o usuário digitar um valor numérico e verificar se é ou não valor um inteiro.
def verificar_inteiro(valor):
    if valor.isdigit():
        return True
    else:
        return False

valor = input("Digite um valor numérico: ")

if verificar_inteiro(valor):
    print("É um número inteiro.")
else:
    print("Não é um número inteiro.")


# Solicitar o usuário digitar uma data ex. 10/10/2021 e exibir 10-10-2010.
def formatar_data(data):
    data_formatada = data.replace('/', '-')
    return data_formatada

data = input("Digite uma data (no formato dd/mm/aaaa): ")

data_formatada = formatar_data(data)

print("Data formatada:", data_formatada)

