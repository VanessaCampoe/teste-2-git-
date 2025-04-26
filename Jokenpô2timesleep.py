import random
import time

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha pedra, papel ou tesoura: ").lower()
computador = random.choice(opcoes)

# Contagem estilo "Jokenpô"
print("\nJO...")
time.sleep(0.5)
print("KEN...")
time.sleep(0.5)
print("PÔ!!!\n")
time.sleep(0.3)

print(f"Você escolheu: {jogador}")
print(f"O computador escolheu: {computador}\n")

if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("Você venceu!")
elif jogador in opcoes:
    print("Você perdeu!")
else:
    print("Opção inválida!")
