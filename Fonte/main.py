from constantes import *
from modulos import *

print("-=-" * 30)
print("-=-" * 30)
print("-=-" * 11, "BEM VINDO AO GEMAS!","-=-" * 12)
print("-=-" * 30)
print("-=-" * 30)

def main():

    pontos = 0

    while True:
        nivel_jogo = input("Digite em qual nível do jogo você quer jogar [Fácil], [Médio] ou [Difícil]: ").lower()
        if nivel_jogo == "fácil" or nivel_jogo == "facil":
            num_linhas = num_colunas = 3
            break
        elif nivel_jogo == "médio" or nivel_jogo == "medio":
            num_linhas = num_colunas = 6
            break
        elif nivel_jogo == "difícil" or nivel_jogo == "dificil":
            num_linhas = num_colunas = 9
            break
        else:
            print("Digite um nível válido")
    while True:
        num_cores = int(input("Digite a quantidade de cores por tabuleiro [3-10]: "))
        if num_cores >= 3 and num_cores <= 10:
            criar(num_linhas, num_colunas, num_cores)
            imprimir(tabuleiro, junt1, num_linhas)
            break
    print(INSTRUCOES)

    while True:
        passe = input("Digite uma das opções [T], [D], ou [S]: ").upper()
        if passe != "T" and passe != "D" and passe != "S":
            print("Digite um comando válido!")
        else:
            if passe == "T":
                print("função troca ainda será criada")
                break
            elif passe == "D":
                print("função dica ainda será criada")
                break
            elif passe == "S":
                print("Obrigada por participar do jogo!")
                break
main()
