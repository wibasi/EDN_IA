# Programa para verificar se um ano é bissexto

# Simulando a entrada do usuário (substitua pelo input() se for rodar localmente)
ano = 2025 # Exemplo de ano bissexto
#ano = 2024 # Exemplo de ano bissexto
#ano = 2023 # Exemplo de ano não bissexto
# ano = 2000 # Exemplo de ano bissexto (divisível por 400)
# ano = 1900 # Exemplo de ano não bissexto (divisível por 100, mas não por 400)

print(f"Verificando o ano: {ano}")

# Lógica para determinar se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} É bissexto.")
else:
    print(f"O ano {ano} NÃO é bissexto.")
    