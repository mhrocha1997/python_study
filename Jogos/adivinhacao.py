import random
def jogar():
    print('******************************************')
    print('Olá, seja bem-vindo ao jogo de adivinhação')
    print('******************************************')

    numero_secreto = random.randrange(1,101)

    print("Qual o nível de dificuldade?")
    print("(1) fácil (2) médio (3) difícil")

    nivel = int(input("Defina o nível: "))

    total_tentativas = 0
    pontos = 1000

    if(nivel==1):
        total_tentativas = 20
    elif(nivel==2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1 ):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = input("Digite o número entre 1 e 100: ")

        print("Você digitou ", chute)
        chute = int(chute)

        if(chute<1 or chute>100):
            print("Digite um numero entre 1 e 100!")
            continue
        acertou = chute == numero_secreto
        maior   = chute>numero_secreto
        menor   = chute<numero_secreto

        if (acertou):
            print("Acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Seu chute foi maior do que número correto")
            elif(menor):
                print("Seu chute foi menor do que o número correto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos-pontos_perdidos
    print("Fim do jogo e fez {}".format(pontos))

if(__name__=="__main__"):
    jogar()