from constantes import *
from modulos import *

print("-=-" * 30)
print("-=-" * 30)
print("-=-" * 11, "BEM VINDO AO GEMAS!","-=-" * 12)
print("-=-" * 30)
print("-=-" * 30)

print(INSTRUCOES)

print("-=-" * 11, "VAMOS COMEÇAR O JOGO!","-=-" * 12)
print()

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
            print("Digite um nível válido!")
    while True:
        try:
            num_cores = int(input("Digite a quantidade de cores por tabuleiro [3-10]: "))
            if num_cores >= 3 and num_cores <= 10:
                break
            else:
                print("Digite um número de cores válido!")
        except ValueError:
            print("Digite um número de cores válido!")

    criar(num_linhas, num_colunas, num_cores, tabuleiro)
    imprimir(tabuleiro, junt1, num_linhas)
    print()

    while True:
        passe = input("Digite uma das opções [T], [D], ou [S]: ").upper()
        if passe != "T" and passe != "D" and passe != "S":
            print("Digite um comando válido!")
        else:
            if passe == "T":
                while True:
                    try:
                        linha1 = int(input("Digite a linha em que se localiza a primeira gema: "))
                        if linha1 <= len(tabuleiro):
                            break
                        else:
                            print("Digite um valor dentro do tamanho do tabuleiro!")
                    except ValueError:
                        print("Só são aceitos valores inteiros!")
                while True:
                    try:
                        coluna1 = int(input("Digite a coluna em que se localiza a primeira gema: "))
                        if coluna1 <= len(tabuleiro):
                            break
                        else:
                            print("Digite um valor dentro do tamanho do tabuleiro!")
                    except ValueError:
                        print("Só são aceitos valores inteiros!")
                while True:
                    try:
                        linha2 = int(input("Digite a linha em que se localiza a segunda gema: "))
                        if linha2 <= len(tabuleiro):
                            break
                        else:
                            print("Digite um valor dentro do tamanho do tabuleiro!")
                    except ValueError:
                        print("Só são aceitos valores inteiros!")
                while True:
                    try:
                        coluna2 = int(input("Digite a coluna em que se localiza a segunda gema: "))
                        if coluna2 <= len(tabuleiro):
                            break
                        else:
                            print("Digite um valor dentro do tamanho do tabuleiro!")
                    except ValueError:
                        print("Só são aceitos valores inteiros!")
                print()
                resultado = validartroca(linha1, coluna1, linha2, coluna2, tabuleiro)
                if resultado == False:
                    print("As posições informadas são de gemas que não estão ao lado ou abaixo uma da outra, informe novas posições")
                else:
                    trocar(linha1, coluna1, linha2, coluna2, tabuleiro)
                    imprimir(tabuleiro, junt1, num_linhas)
                    print()
            elif passe == "D":
                print("função dica ainda será criada")
                break
            elif passe == "S":
                print("Obrigada por participar do jogo!")
                break
main()
