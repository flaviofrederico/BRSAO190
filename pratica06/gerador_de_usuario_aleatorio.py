"""Gerador de Usuário Aleatório  
Crie um programa que acessa uma API pública e exibe informações de um usuário fictício. Para isso:

* Use a API pública "https://randomuser.me/api/" para obter dados aleatórios.  
* Mostre na tela: nome completo, e-mail e país do usuário.  
* O programa deve tratar possíveis erros de conexão ou falha na API.  

Dica: Utilize o módulo `requests` para fazer a requisição e o método `.json()` para acessar os dados."""

import requests
from pprint import pprint  

def gerar_usuario():
    print("\nGERADOR DE USUÁRIO ALEATÓRIO")
    
    try:
       
        resposta = requests.get(
            "https://randomuser.me/api/",
            timeout=10  
        )
        resposta.raise_for_status() 
        
        dados = resposta.json()
        usuario = dados['results'][0]
        
        print("\nDados do Usuário:")
        print(f"Nome: {usuario['name']['first']} {usuario['name']['last']}")
        print(f"Email: {usuario['email']}")
        print(f"País: {usuario['location']['country']}")
        
    except requests.exceptions.RequestException as e:
        print(f"\n Erro na conexão: {e}")
    except KeyError:
        print("\n A API retornou dados inesperados")

gerar_usuario()