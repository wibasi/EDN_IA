def verificar_senha(senha):
    if len(senha) < 8:
        return "Senha inválida: deve ter pelo menos 8 caracteres."
    
    if not any(char.isdigit() for char in senha):
        return "Senha inválida: deve conter pelo menos um número."

    return "Senha válida!"

senha = input("Digite sua senha: ")
resultado = verificar_senha(senha)
print(resultado)
