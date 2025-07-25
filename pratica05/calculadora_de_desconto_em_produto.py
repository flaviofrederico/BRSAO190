"""Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.
"""

def calcular_desconto_produto(preco, percentual):
    return preco * (1 - percentual / 100)

preco_original = float(input("Digite o preço original do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

preco_final = calcular_desconto_produto(preco_original, percentual_desconto)

print(f"Preço final com desconto: R$ {preco_final:.2f}")