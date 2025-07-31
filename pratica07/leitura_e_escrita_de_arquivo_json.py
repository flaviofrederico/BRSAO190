"""4- Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.
"""

import json
import os

dados_pessoa = {
    "nome": "João Silva",
    "idade": 30,
    "cidade": "São Paulo",
    "profissao": "Engenheiro"
}

try:
    if not os.path.exists('pratica07'):
        os.makedirs('pratica07')

    nome_arquivo = input("Digite o nome do arquivo JSON (sem extensão): ") + ".json"
    caminho_completo = os.path.join('pratica07', nome_arquivo)
    
    with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados_pessoa, arquivo, ensure_ascii=False, indent=4)
    print(f"Dados salvos com sucesso no arquivo {caminho_completo}!")
    
    with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
        dados_carregados = json.load(arquivo)
    
    print("\nDados carregados do arquivo:")
    for chave, valor in dados_carregados.items():
        print(f"{chave.capitalize()}: {valor}")
        
except PermissionError:
    print("Erro: Permissão negada para escrever no arquivo.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")