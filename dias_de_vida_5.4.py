from datetime import datetime

def calcular_dias_vivo(data_nascimento: str) -> int:
    # Converte a string para data no formato dd/mm/aaaa
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.today()
    dias_vivo = (hoje - nascimento).days
    return dias_vivo

# Interação com o usuário
data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dias = calcular_dias_vivo(data)
print(f"Você está vivo há aproximadamente {dias} dias.")
