# Programa de conversão de moedas
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Calculando as conversões
valor_dolares = valor_reais / taxa_dolar
valor_euros = valor_reais / taxa_euro

# Exibindo os resultados
print("=== CONVERSOR DE MOEDAS ===")
print(f"Valor original: R$ {valor_reais:.2f}")
print(f"Taxa do dólar: R$ {taxa_dolar:.2f}")
print(f"Taxa do euro: R$ {taxa_euro:.2f}")
print()
print("=== CONVERSÕES ===")
print(f"Em dólares: US$ {valor_dolares:.2f}")
print(f"Em euros: € {valor_euros:.2f}")