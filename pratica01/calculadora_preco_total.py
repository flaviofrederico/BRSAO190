"""4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preco total de uma compra.
* Use as seguintes informações:

* Nome do produto: "cadeira Infantil"
* Preço unitário: R$ 12.40
*

Quantidade: 3

* O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

nome_do_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

preco_total = preco_unitario * quantidade

print(f"Produto: {nome_do_produto}")
print(f"Preço unitário: R${preco_unitario: .2f}")
print(f"Quantidade: {quantidade}")
print(f"O preço total do produto {nome_do_produto} é R${preco_total: .2f}")