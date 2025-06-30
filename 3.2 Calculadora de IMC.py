# Programa para calcular o IMC (Índice de Massa Corporal)

peso = 70.0  # kg
altura = 1.75  # metros

# Calculando o IMC
imc = peso / (altura ** 2)

# Classificando o IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Exibindo os resultados
print("=== CALCULADORA DE IMC ===")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print()
print(f"IMC calculado: {imc:.2f}")
print(f"Classificação: {classificacao}")
print()
print("=== TABELA DE REFERÊNCIA ===")
print("< 18.5: Abaixo do peso")
print("18.5 - 24.9: Peso normal")
print("25.0 - 29.9: Sobrepeso")
print("≥ 30.0: Obeso")