import json

produto_01 = {
    "nome":"sapato",
    "quantidade":10,
    "preco":20.99,
    "disponibilidade": True
}

produto_02 = {
    "nome":"tenis",
    "quantidade":20,
    "preco":89.99,
    "disponibilidade": False
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

carrinhio_json = json.dumps(carrinho)
print(carrinhio_json)