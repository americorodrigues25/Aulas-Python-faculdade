produtos = ["nike", "adidas", "vans", "calvin", "starter", "element"]
produtos.sort()
for i in range(3):
    print(produtos[i])

#................... EXERCICIO 1 ......................


for i in range(10):
    i+=1
    if i %2:
        print(i, "Numero é impar")
    else:
        print(i, "Numero é par") 

#................... EXERCICIO 2 ......................


soma=0
for i in range(3):
    notas = int(input("Escreva sua nota: "))
    soma+=notas
print("Esta é sua média final: ", soma/3)

#................... EXERCICIO 3 ......................


tabuada = int(input("Digite um numero até 10: "))
for i in range(10):
    print(tabuada, "x", i, "=", (tabuada * i))

#................... EXERCICIO 4 ......................
    

produto = int(input("Digite o valor do seu produto: "))
for i in range(24):
    i+=2
    print(produto, "x", i, "=", (produto / i))

#................... EXERCICIO 5 ......................
