# Programa de cálculo de média escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# Calculando a média
media = (nota1 + nota2 + nota3) / 3

# Exibindo os resultados
print("=== CALCULADORA DE MÉDIA ESCOLAR ===")
print(f"Nota 1: {nota1:.1f}")
print(f"Nota 2: {nota2:.1f}")
print(f"Nota 3: {nota3:.1f}")
print()
print("=== RESULTADO ===")
print(f"Média final: {media:.2f}")
print()

# Verificando a situação do aluno
if media >= 7.0:
    print("✅ Situação: APROVADO")
elif media >= 5.0:
    print("⚠️ Situação: RECUPERAÇÃO")
else:
    print("❌ Situação: REPROVADO")