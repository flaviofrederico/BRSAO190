"""4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preco total de uma compra.
* Use as seguintes informações:

* Nome do produto: "cadeira Infantil"
* Preço unitário: R$ 12.40
*

Quantidade: 3

* O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

Nome_do_produto= "cadeira Infantil"
Preco_unitario = 12.40
Quantidade = 3

Preco_total = Preco_unitario * Quantidade

print(f"Produto:{Nome_do_produto}")
print(f"Preço unitário: R${Preco_unitario: .2f}")
print(f"Quantidade:{Quantidade}")
print(f"O preço do total do produto {Nome_do_produto} é R${Preco_total: .2f}")