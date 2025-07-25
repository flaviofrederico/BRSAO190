"""Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final."""


from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365

try:
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    if ano_nascimento > datetime.now().year:
        print("Ano de nascimento não pode ser maior que o ano atual!")
    else:
        idade_dias = calcular_idade_em_dias(ano_nascimento)
        print(f"Sua idade em dias (aproximada) é: {idade_dias} dias")
except ValueError:
    print("Por favor, digite um ano válido!")