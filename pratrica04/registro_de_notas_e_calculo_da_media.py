"""Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".  
* Somente notas entre 0 e 10 devem ser aceitas.  
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.  
* Trate entradas inválidas com mensagens de erro."""

notas = []
total_notas = 0

print("Digite as notas (0 a 10) ou 'fim' para terminar:")

while True:
    entrada = input("Nota: ")
    
    if entrada.lower() == 'fim':
        if total_notas == 0:
            print("Nenhuma nota foi registrada.")
        else:
            media = sum(notas) / total_notas
            print(f"Média da turma: {media:.2f}")
            print(f"Total de notas válidas registradas: {total_notas}")
        break
    
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
            total_notas += 1
        else:
            print("Erro: A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Erro: Por favor, digite um número válido ou 'fim'.")