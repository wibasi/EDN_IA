def calcular_preco_final(preco_original: float, desconto_percentual: float) -> float:
    valor_desconto = preco_original * (desconto_percentual / 100)
    preco_final = preco_original - valor_desconto
    return round(preco_final, 2)

# Interação com o usuário
preco = float(input("Digite o preço original do produto: R$ "))
desconto = float(input("Digite o percentual de desconto (%): "))

preco_com_desconto = calcular_preco_final(preco, desconto)
print(f"Preço final com desconto: R$ {preco_com_desconto:.2f}")

