import os
os.system("cls")

corredores = {}

for i in range(5):
    nome = input(f"Digite o nome do corredor {i + 1}: ")
    voltas = []
    
    for j in range(3):
        while True:
            try:
                tempo = float(input(f"Digite o tempo da volta {j + 1} de {nome}: "))
                if tempo < 0:
                    print("O tempo deve ser um valor positivo. Tente novamente.")
                else:
                    voltas.append(tempo)
                    break
            except ValueError:
                print("Entrada inválida! Por favor, insira um número.")

    corredores[nome] = voltas

print("\nMédia de tempo de cada corredor:")
for nome, voltas in corredores.items():
    media = sum(voltas) / len(voltas)
    print(f"{nome}: média de tempo = {media:.3f} segundos")