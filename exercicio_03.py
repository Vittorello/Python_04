#  3 - Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

from typing import Dict, Any

livro: Dict[str,Any] = {
    "Titulo":"Menos achismo, Mais dados",
    "Autor": "Igor Camargo Vitorello",
    "Ano":"2000"
}

lista_de_elementos: list =livro.items()
for livro in lista_de_elementos:
    print(livro)