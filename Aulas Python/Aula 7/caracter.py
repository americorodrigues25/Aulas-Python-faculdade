def caracter(texto):
    print(len(texto))
    if texto.isdigit ():
        print("Tem número")
    else:
        print("Não tem número")

        if texto.isalnum ():
            print ("É alfanumerico")
        else:
            print("Não é alfanumerico")
        if texto.startswith ("A"):
            print("Começa com A")
        else:
            print ("Não começa com A")

textos = input ("Digite um texto: ")
caracter(textos)