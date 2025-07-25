"""Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for."""

def palindromo(texto):
    texto = ''.join(c for c in texto.lower() if c.isalnum())
    return texto == texto[::-1]

entrada = input("Digite uma palavra ou frase: ")
print("Sim" if palindromo(entrada) else "Não")