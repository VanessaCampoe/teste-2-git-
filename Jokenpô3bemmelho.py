import random
import time

opcoes = ["pedra", "papel", "tesoura"]

print("Escolha uma opção:")
print("[1] Pedra")
print("[2] Papel")
print("[3] Tesoura")

escolha = input("Digite o número da sua escolha: ")

# Verifica se o número é válido
if escolha in ["1", "2", "3"]:
    jogador = opcoes[int(escolha) - 1]
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
    else:
        print("Você perdeu!")
else:
    print("Opção inválida! Escolha 1, 2 ou 3.")
