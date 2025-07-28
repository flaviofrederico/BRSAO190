"""Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`."""

import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def converter_moeda():
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip().upper()
    
    if len(moeda) != 3 or not moeda.isalpha():
        print("Código inválido. Use 3 letras.")
        return
    
    try:
        api_key = os.getenv('AWESOMEAPI_KEY')
        url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        if api_key:
            url += f"?apikey={api_key}"
        
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()[f"{moeda}BRL"]
        
        print(f"\nCotação atual: R$ {float(dados['bid']):.4f}")
        print(f"Valor máximo: R$ {float(dados['high']):.4f}")
        print(f"Valor mínimo: R$ {float(dados['low']):.4f}")
        print(f"Última atualização: {datetime.fromtimestamp(int(dados['timestamp'])).strftime('%d/%m/%Y %H:%M')}")
    
    except requests.exceptions.RequestException:
        print("Erro na conexão com a API")
    except KeyError:
        print("Moeda não encontrada ou dados inválidos")

converter_moeda()