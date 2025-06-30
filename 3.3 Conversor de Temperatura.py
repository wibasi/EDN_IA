# Conversor de Temperaturas

def converter_temperatura(valor, origem, destino):
    # Converte a temperatura para Celsius primeiro
    if origem == "C":
        temp_c = valor
    elif origem == "F":
        temp_c = (valor - 32) / 1.8
    elif origem == "K":
        temp_c = valor - 273.15
    else:
        return "Unidade de origem inválida."

    # Converte de Celsius para a unidade de destino
    if destino == "C":
        return temp_c
    elif destino == "F":
        return temp_c * 1.8 + 32
    elif destino == "K":
        return temp_c + 273.15
    else:
        return "Unidade de destino inválida."

# Exemplo de uso:
valor = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").strip().upper()
destino = input("Unidade de destino (C/F/K): ").strip().upper()

resultado = converter_temperatura(valor, origem, destino)

if isinstance(resultado, str):
    print(resultado)
else:
    print(f"{valor:.2f} {origem} = {resultado:.2f} {destino}")
  