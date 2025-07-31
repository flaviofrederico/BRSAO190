"""
3- Leitura de Arquivo CSV  
Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela. Para isso:

* Solicite ao usuário o nome do arquivo CSV a ser lido.  
* Utilize o módulo `csv` para abrir o arquivo e ler os dados.  
* Exiba cada linha completa como uma lista.  
* Trate erros como arquivo inexistente ou problemas na leitura.

Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.
"""

import csv
import os

def detectar_delimitador(caminho_arquivo):
    
    with open(caminho_arquivo, 'r', encoding='utf-8-sig') as arquivo:
        primeira_linha = arquivo.readline()
        return ';' if ';' in primeira_linha and ',' not in primeira_linha.replace('.', '') else ','

nome_arquivo = input("Digite o nome do arquivo CSV (com extensão): ").strip()
caminho_completo = os.path.join('pratica07', nome_arquivo)

try:
    if not os.path.exists('pratica07'):
        os.makedirs('pratica07')

    if not os.path.exists(caminho_completo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_completo}")

    delimitador = detectar_delimitador(caminho_completo)

    with open(caminho_completo, 'r', encoding='utf-8-sig') as arquivo:
        leitor = csv.reader(arquivo, delimiter=delimitador)
        
        cabecalho = next(leitor)
        print("\nCabeçalho:", cabecalho)

        for i, linha in enumerate(leitor, 1):
            linha_limpa = [campo.strip().replace('\ufeff', '') for campo in linha]
            print(f"Linha {i}: {linha_limpa}")
        
        print(f"\nTotal de registros: {i}")

except FileNotFoundError as e:
    print(f"\nErro: {e}")
except PermissionError:
    print("\nErro: Permissão negada para ler o arquivo.")
except UnicodeDecodeError:
    print("\nErro: Problema de codificação do arquivo.")
except csv.Error as e:
    print(f"\nErro no CSV: {e}")
except Exception as e:
    print(f"\nErro inesperado: {e}")