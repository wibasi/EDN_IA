import re

def eh_palindromo(texto: str) -> str:
    # Remove espaços e pontuação, e converte para minúsculas
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    # Verifica se é igual ao reverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplo de uso
frase = input("Digite uma palavra ou frase: ")
print(eh_palindromo(frase))
