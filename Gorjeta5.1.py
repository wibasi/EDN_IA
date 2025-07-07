def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso
valor = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))
valor_gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
