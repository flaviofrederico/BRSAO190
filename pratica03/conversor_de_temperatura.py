"""Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""

temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Unidade de origem (C, F, K): ").upper()
unidade_destino = input("Unidade de destino (C, F, K): ").upper()

# Converter para Celsius primeiro
if unidade_origem == 'C':
    celsius = temperatura
elif unidade_origem == 'F':
    celsius = (temperatura - 32) * 5/9
elif unidade_origem == 'K':
    celsius = temperatura - 273.15
else:
    print("Unidade de origem inválida!")
    exit()

# Converter de Celsius para unidade de destino
if unidade_destino == 'C':
    resultado = celsius
elif unidade_destino == 'F':
    resultado = celsius * 9/5 + 32
elif unidade_destino == 'K':
    resultado = celsius + 273.15
else:
    print("Unidade de destino inválida!")
    exit()

print(f"{temperatura} {unidade_origem} = {resultado:.2f} {unidade_destino}")