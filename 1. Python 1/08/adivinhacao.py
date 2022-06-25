import random

def jogar():

    print("Bem vindo!")

    # numero_secreto = round(random.random()*100)
    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade ?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha o nível: "))

    if(nivel == 1):
        tentativas = 20
    if(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

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
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou, o chute é maior que o número!")
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou, o chute é menor que o número!")
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()