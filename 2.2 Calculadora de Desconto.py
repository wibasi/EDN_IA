# Programa de cálculo de desconto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Calculando o desconto e preço final
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibindo os resultados
print("=== CALCULADORA DE DESCONTO ===")
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto aplicado: {porcentagem_desconto}%")
print()
print("=== DETALHES DO DESCONTO ===")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
print()
print(f"Você economizou R$ {valor_desconto:.2f}!")