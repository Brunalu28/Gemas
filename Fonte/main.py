from constantes import *
from modulos import *

print(""" {}

░█▀▀█ ░█▀▀▀ ░█▀▄▀█ 　 ░█──░█ ▀█▀ ░█▄─░█ ░█▀▀▄ ░█▀▀▀█ 　 ─█▀▀█ ░█▀▀▀█ 　 ░█▀▀█ ░█▀▀▀ ░█▀▄▀█ ─█▀▀█ ░█▀▀▀█ █ 
░█▀▀▄ ░█▀▀▀ ░█░█░█ 　 ─░█░█─ ░█─ ░█░█░█ ░█─░█ ░█──░█ 　 ░█▄▄█ ░█──░█ 　 ░█─▄▄ ░█▀▀▀ ░█░█░█ ░█▄▄█ ─▀▀▀▄▄ ▀ 
░█▄▄█ ░█▄▄▄ ░█──░█ 　 ──▀▄▀─ ▄█▄ ░█──▀█ ░█▄▄▀ ░█▄▄▄█ 　 ░█─░█ ░█▄▄▄█ 　 ░█▄▄█ ░█▄▄▄ ░█──░█ ░█─░█ ░█▄▄▄█ ▄{}
""".format(cores["azul"], cores["limpa"]))

print(INSTRUCOES)

print(cores["vermelho"], "-=-" * 12, "VAMOS COMEÇAR O JOGO!","-=-" * 12, cores["limpa"])
print()

# função principal do jogo


def main():

    pontos = 0

    while True:
        try:
            num_linhas = num_colunas = int(input("Digite a quantidade de linhas e colunas do tabuleiro [Fácil: 3-6] [Médio: 6-8] [Difícil: 8-10]: "))
            if num_linhas >= MIN_TABULEIRO and num_linhas <= MAX_TABULEIRO:
                break
            else:
                print("{}Digite um valor entre 3 e 10!{}".format(cores["vermelho"], cores["limpa"]))
        except ValueError:
            print("{}Digite um valor correspondente as linhas e colunas do tabuleiro!{}".format(cores["vermelho"], cores["limpa"]))

    while True:
        try:
            num_cores = int(input("Digite a quantidade de cores por tabuleiro [3-26]: "))
            if num_cores >= MIN_CORES and num_cores <= MAX_CORES:
                break
            else:
                print("{}Digite um número de cores válido!{}".format(cores["vermelho"], cores["limpa"]))
        except ValueError:
            print("{}Digite um número de cores válido!{}".format(cores["vermelho"], cores["limpa"]))

    limpaTela()

    coresEscolhidas = criacores(num_cores)
    tabuleiro = criar(num_linhas, num_colunas, coresEscolhidas)


    # verifica se existem cadeias na vertical já formadas, pois na função criar as cadeias já formadas da horizontal já estão tiradas

    while True:
        cadeiasVerticais(tabuleiro)
        eliminadas = peçasEliminadas(tabuleiro)
        if eliminadas == 0:
            imprimir(tabuleiro)
            break
        else:
            tabuleiro = criar(num_linhas, num_colunas, coresEscolhidas)
    print()

    while True:
        passe = input("Digite uma das opções [T], [D], [I], [TA], ou [S]: ").upper()
        if passe != "T" and passe != "D" and passe != "S" and passe != "TA" and passe != "I":
            print("{}Digite um comando válido!{}".format(cores["vermelho"], cores["limpa"]))
        else:
            if passe == "T":
                while True:
                    try:
                        linha1 = int(input("Digite a linha em que se localiza a primeira gema: "))
                        if linha1 <= len(tabuleiro):
                            break
                        else:
                            print("{}Digite um valor dentro do tamanho do tabuleiro!{}".format(cores["vermelho"], cores["limpa"]))
                    except ValueError:
                        print("{}Só são aceitos valores inteiros!{}".format(cores["vermelho"], cores["limpa"]))
                while True:
                    try:
                        coluna1 = int(input("Digite a coluna em que se localiza a primeira gema: "))
                        if coluna1 <= len(tabuleiro):
                            break
                        else:
                            print("{}Digite um valor dentro do tamanho do tabuleiro!{}".format(cores["vermelho"], cores["limpa"]))
                    except ValueError:
                        print("{}Só são aceitos valores inteiros!{}".format(cores["vermelho"], cores["limpa"]))
                while True:
                    try:
                        linha2 = int(input("Digite a linha em que se localiza a segunda gema: "))
                        if linha2 <= len(tabuleiro):
                            break
                        else:
                            print("{}Digite um valor dentro do tamanho do tabuleiro!{}".format(cores["vermelho"], cores["limpa"]))
                    except ValueError:
                        print("{}Só são aceitos valores inteiros!{}".format(cores["vermelho"], cores["limpa"]))
                while True:
                    try:
                        coluna2 = int(input("Digite a coluna em que se localiza a segunda gema: "))
                        if coluna2 <= len(tabuleiro):
                            break
                        else:
                            print("{}Digite um valor dentro do tamanho do tabuleiro!{}".format(cores["vermelho"], cores["limpa"]))
                    except ValueError:
                        print("{}Só são aceitos valores inteiros!{}".format(cores["vermelho"], cores["limpa"]))
                print()
                resultado = validartroca(linha1, coluna1, linha2, coluna2)
                if resultado == False:
                    print("{}As posições informadas são de gemas que não estão ao lado ou abaixo uma da outra, informe novas posições.{}".format(cores["vermelho"], cores["limpa"]))
                else:
                    trocar(linha1, coluna1, linha2, coluna2, tabuleiro)
                    powerup4e5_colunas(tabuleiro)
                    powerup4e5_linhas(tabuleiro)
                    cadeiasHorizontais(tabuleiro)
                    cadeiasVerticais(tabuleiro)
                    eliminadas = peçasEliminadas(tabuleiro)
                    if eliminadas > 0:
                        print("{}Você eliminou um total de {} gemas!{}".format(cores["verde"], eliminadas, cores["limpa"]))
                    else:
                        print("{}Você não eliminou nenhuma gema!{}".format(cores["vermelho"], cores["limpa"]))
                    desloca(tabuleiro)
                    preencher(tabuleiro, coresEscolhidas, num_cores)
                    imprimir(tabuleiro)
                    print()
                    pontos += eliminadas
            elif passe == "D":
                pontos -= 1
                while True:
                    try:
                        op_dicas = input("Digite se deseja dicas de permutações para linhas ou colunas[L ou C]: ").upper()
                        if op_dicas == "L":
                            dicasdojogo_horizontal(tabuleiro)
                            break
                        elif op_dicas == "C":
                            dicasdojogo_vertical(tabuleiro)
                            break
                        else:
                            print("{}Digite uma opção válida!{}".format(cores["vermelho"], cores["limpa"]))
                    except ValueError:
                        print("{}Só são aceitos valores inteiros!{}".format(cores["vermelho"], cores["limpa"]))
            elif passe == "S":
                print("Obrigada por participar!")
                if pontos > 0:
                    print("{}Parabéns! Você obteve um total de {} pontos! :){}".format(cores["verde"], pontos, cores["limpa"]))
                else:
                    print("{}Que triste, você perdeu o jogo, e ficou com {} pontos! :({}".format(cores["vermelho"], pontos, cores["limpa"]))
                break
            elif passe == "TA":
                imprimir(tabuleiro)
                print()
            elif passe == "I":
                print(INSTRUCOES)
main()
