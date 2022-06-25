import random

print("Bem vindo!")

# numero_secreto = round(random.random()*100)
numero_secreto = random.randrange(1, 100)
tentativas = 3

print(numero_secreto)

for rodada in range(1, tentativas + 1):

    print("Tentativa {} de {}".format(rodada, tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Entrada inválida, digite um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou, o chute é maior que o número!")
        elif(menor):
            print("Você errou, o chute é menor que o número!")

print("Fim de jogo!")
