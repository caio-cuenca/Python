import random

def abertura():
    print("Bem vindo!")

def palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()

def letras(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def chutar():
    chute = input("Digite uma letra: ")
    return chute.strip().upper()

def marcar_acerto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
    return letras_acertadas

def finalizar(acertou, palavra_secreta):
    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu! A palavra era", palavra_secreta)

def jogar():
    abertura()
    palavra_secreta = palavra()
    letras_acertadas = letras(palavra_secreta)
    print("A palavra é: ", letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = chutar()

        if(chute in palavra_secreta):
            letras_acertadas = marcar_acerto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            print("Você errou, faltam", 4 - erros, "chances")

        enforcou = erros == 4
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    finalizar(acertou, palavra_secreta)

if(__name__ == "__main__"):
    jogar()