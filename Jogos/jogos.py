import forca
import adivinhacao

print('******************************************')
print('Escolha o seu jogo')
print('******************************************')

print('(1) forca (2) adivinhação')
jogo = int(input('Qual o jogo?'))

if(jogo ==1):
    print("Jogando Forca")
    forca.jogar()
elif(jogo==2):
    print("jogando adivinhação")
    adivinhacao.jogar()