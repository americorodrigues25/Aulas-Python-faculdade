class Produto:
    def __init__(self, codigo, descricao, preco, quantidade):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def ExibirDescricao_Preco(self):
        return f"Descrição: {self.descricao}, Preço: R${self.preco}"

    def ExibirQuantidade(self):
        return f"Quantidade: {self.quantidade}"

    def ExibirTipoProduto(self, preco):
        if preco > 500:
            return "Não Acessível"
        else:
            return "Acessível"


class Bolsa(Produto):
    def __init__(self, codigo, descricao, preco, quantidade, marca, material):
        super().__init__(codigo, descricao, preco, quantidade)
        self.marca = marca
        self.material = material

    def ExibirMarca(self):
        return f"Marca: {self.marca}"

    def ExibirMaterial(self):
        return f"Material: {self.material}"


bolsa1 = Bolsa(codigo=1, descricao="Bolsa de couro", preco=450, quantidade=10, marca="MarcaX", material="Couro")
print(bolsa1.ExibirDescricao_Preco())
print(bolsa1.ExibirQuantidade())
print(bolsa1.ExibirTipoProduto(bolsa1.preco))
print(bolsa1.ExibirMarca())
print(bolsa1.ExibirMaterial())
