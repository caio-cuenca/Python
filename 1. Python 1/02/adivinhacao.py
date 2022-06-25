print("Bem vindo!")

numero_secreto = 42
chute_str = input("Digite um número: ")

print("Você digitou: ", chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")

print("Fim de jogo!")
