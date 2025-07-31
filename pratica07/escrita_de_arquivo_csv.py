"""Escrita de Arquivo CSV  
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha."""


import csv
import os

dados_pessoas = [
    ["Flávio Frederico", 30, "São Paulo"],
    ["Arão Gomes", 29, "Curitiba"],
    ["António Eduardo", 30, "Bahia"],
    ["Alice José", 24, "Ceará"],
    ["Tanico Kussumba", 27, "Espírito Santo"],
    ["Suzeth Joaquim", 25, "Maranhão"],
    ["Lilson Smith", 28, "Rio de Janeiro"]
]

try:
    if not os.path.exists('pratica07'):
        os.makedirs('pratica07')
    
    nome_arquivo = input("Digite o nome do arquivo CSV para salvar os dados (sem extensão): ").strip()
    
    if not nome_arquivo.lower().endswith('.csv'):
        nome_arquivo += '.csv'
    
    caminho_completo = os.path.join('pratica07', nome_arquivo)
    
    with open(caminho_completo, mode='w', newline='', encoding='utf-8-sig') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')  
        escritor.writerow(["Nome", "Idade", "Cidade"])
        escritor.writerows(dados_pessoas)
    
    print(f"Dados salvos com sucesso no arquivo '{caminho_completo}'!")

except PermissionError:
    print("Erro: Permissão negada para escrever no arquivo.")
except IOError as e:
    print(f"Erro ao escrever no arquivo: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")