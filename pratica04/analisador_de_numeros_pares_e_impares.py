"""Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas.  """

pares = 0
impares = 0

print("Digite números inteiros ou 'fim' para terminar o programa:")

while True:
    entrada = input("Número: ")
    
    if entrada.lower() == 'fim':
        print(f"Programa encerrado!")
        print(f"Total de números pares: {pares}")
        print(f"Total de números ímpares: {impares}")
        break
    
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é um número par.")
            pares += 1
        else:
            print(f"{numero} é um número ímpar.")
            impares += 1
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido ou 'fim'.")