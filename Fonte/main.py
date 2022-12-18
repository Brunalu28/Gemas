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
        try:
            num_linhas = num_colunas = int(input("Digite a quantidade de linhas e colunas do tabuleiro [Fácil: 3-6] [Médio: 6-8] [Difícil: 8-10]: "))
            if num_linhas >= MIN_TABULEIRO and num_linhas <= MAX_TABULEIRO:
                break
            else:
                print("Digite um valor entre 3 e 10!")
        except ValueError:
            print("Digite um valor correspondente as linhas e colunas do tabuleiro!")

    while True:
        try:
            num_cores = int(input("Digite a quantidade de cores por tabuleiro [3-26]: "))
            if num_cores >= MIN_CORES and num_cores <= MAX_CORES:
                break
            else:
                print("Digite um número de cores válido!")
        except ValueError:
            print("Digite um número de cores válido!")

    coresEscolhidas = criacores(num_cores)
    tabuleiro = criar(num_linhas, num_colunas, coresEscolhidas)
    while True:
        cadeiasVerticais(tabuleiro)
        eliminadas = peçasEliminadas(tabuleiro)
        if eliminadas > 0:
            tabuleiro = criar(num_linhas, num_colunas, coresEscolhidas)
        else:
            imprimir(tabuleiro)
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
                            powerup4_linhas(tabuleiro)
                            powerup4_colunas(tabuleiro)
                            powerup5_colunas(tabuleiro)
                            powerup5_linhas(tabuleiro)
                            cadeiasHorizontais(tabuleiro)
                            cadeiasVerticais(tabuleiro)
                            eliminadas = peçasEliminadas(tabuleiro)
                            if eliminadas > 0:
                                print("Você eliminou um total de {} gemas!".format(eliminadas))
                            else:
                                print("Você não eliminou nenhuma gema!")
                            desloca(tabuleiro)
                            preencher(tabuleiro, coresEscolhidas)
                            imprimir(tabuleiro)
                            print()
                        pontos += eliminadas
                    elif passe == "D":
                        print("função dica ainda será criada")
                        break
                    elif passe == "S":
                        print("Obrigada por participar do jogo!")
                        print("Você obteve um total de {} pontos!".format(pontos))
                        break
main()
