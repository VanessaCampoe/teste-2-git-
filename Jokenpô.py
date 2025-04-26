import random

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha pedra, papel ou tesoura: ").lower()
computador = random.choice(opcoes)

print(f"Você escolheu: {jogador}")
print(f"O computador escolheu: {computador}")

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
