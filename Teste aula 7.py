idade = int(input("Digite sua idade: "))

if idade <= 0:
    print("Idade invalida, digite uma idade valida!!")
elif idade <= 13:
    print("Você é uma criança!!!!!!")
elif idade <= 17:
    print("Você é um adolescente!!!!!!")
elif idade <=59:
    print("Você é um adulto!!!!!!")
else:
    print("Você é idoso!!!!!!")