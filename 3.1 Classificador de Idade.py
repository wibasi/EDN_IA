# Programa de classificação de idade

try:
    idade = int(input("Por favor, digite sua idade: "))

    if idade >= 0 and idade <= 12:
        categoria = "Criança"
    elif idade >= 13 and idade <= 17:
        categoria = "Adolescente"
    elif idade >= 18 and idade <= 59:
        categoria = "Adulto"
    elif idade >= 60:
        categoria = "Idoso"
    else:
        categoria = "Idade inválida (não pode ser negativa)"

    print(f"Você tem {idade} anos e se enquadra na categoria: {categoria}.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para a idade.")