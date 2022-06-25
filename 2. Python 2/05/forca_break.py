def jogar():
    print("Bem vindo!")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False
    erros = 0

    print("A palavra é: ", letras_acertadas)

    while (not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Errou, faltam", 6 - erros, "tentativas")

        if(erros == 6):
            break
        elif("_" not in letras_acertadas):
            break

        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim de jogo!")


if (__name__ == "__main__"):
    jogar()