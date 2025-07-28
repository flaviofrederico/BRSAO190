"""Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`."""

import requests
from dotenv import load_dotenv

load_dotenv()

def consulta_cep():
    cep = input("Digite o CEP (apenas números): ").strip()
    
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido! Digite 8 números.")
        return
    
    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=10)
        dados = resposta.json()
        
        if 'erro' in dados:
            print("CEP não encontrado!")
            return
        
        print(f"\nLogradouro: {dados.get('logradouro', 'N/A')}")
        print(f"Bairro: {dados.get('bairro', 'N/A')}")
        print(f"Cidade: {dados.get('localidade', 'N/A')}")
        print(f"Estado: {dados.get('uf', 'N/A')}")
        print(f"CEP: {dados.get('cep', 'N/A')}")
    
    except requests.exceptions.RequestException:
        print("Erro na conexão. Verifique sua internet.")

consulta_cep()