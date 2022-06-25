print("Bem vindo!")

numero_secreto = 42
tentativas = 3
rodada = 1

while(rodada <= tentativas):

    print("Rodada", rodada, "de", tentativas)

    chute_str = input("Digite um número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou")
    else:
        if(maior):
            print("Você errou, o chute é maior que o número!")
        elif(menor):
            print("Você errou, o chute é menor que o número!")

    rodada = rodada + 1

print("Fim de jogo!")
