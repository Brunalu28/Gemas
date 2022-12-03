# Funções genericas que vão estar presente no jogo

from constantes import *
import random

# Variáveis para as funções

tabuleiro = []
junt1 = ""

# Função que cria o tabuleiro comletras aleatorias do alfabeto que representam as cores das gemas

def criar(num_linhas, num_colunas, num_cores):
    cores_escolhidas = []
    for x in range(num_cores):
        while True:
            op_cores = random.choice(cores_gemas)
            if op_cores not in cores_escolhidas:
                cores_escolhidas.append(op_cores)
                break
    for i in range(num_linhas):
        while True:
            contcores = 0
            linhas = []
            for j in range(num_colunas):
                gemas_validas = random.choice(cores_escolhidas)
                linhas.append(gemas_validas)
            for k in range(1, len(linhas)):
                if linhas[k] == linhas[k-1]:
                    contcores +=1
                    if contcores >= 2:
                        break
                else:
                    contcores = 0
            if contcores < 2:
                tabuleiro.append(linhas)
                break

# Verificando colunas com letras iguais para refazer

    # if len(tabuleiro) == 3:
    #     for i in range(len(tabuleiro)):
    #         for j in range(len(tabuleiro[i])):
    #             if i + 2 < len(tabuleiro):
    #                 if tabuleiro[i][j] == tabuleiro[i+2][j] and tabuleiro[i][j] == tabuleiro[i+1][j]:
    #                     while True:
    #                         gemas_validas = random.choice(cores_escolhidas)
    #                         if gemas_validas != tabuleiro[i][j]:
    #                             tabuleiro[i][j] == gemas_validas
    #                         break
    # if len(tabuleiro) == 6:
    #     for i in range(len(tabuleiro)):
    #         for j in range(len(tabuleiro[i])):
    #             if i + 2 < len(tabuleiro):
    #                 if tabuleiro[i][j] == tabuleiro[i+2][j] and tabuleiro[i][j] == tabuleiro[i+1][j]:
    #                     while True:
    #                         gemas_validas = random.choice(cores_escolhidas)
    #                         if gemas_validas != tabuleiro[i][j]:
    #                             tabuleiro[i][j] == gemas_validas
    #                         break
    #                 if tabuleiro[i+3][j] == tabuleiro[i+4][j] and tabuleiro[i+3][j] == tabuleiro[i+5][j]:
    #                     while True:
    #                         gemas_validas = random.choice(cores_escolhidas)
    #                         if gemas_validas != tabuleiro[i+3][j]:
    #                             tabuleiro[i+3][j] == gemas_validas
    #                         break
    # if len(tabuleiro) == 9:
    #     for i in range(len(tabuleiro)):
    #         for j in range(len(tabuleiro[i])):
    #             if i + 2 < len(tabuleiro):
    #                 if tabuleiro[i][j] == tabuleiro[i+2][j] and tabuleiro[i][j] == tabuleiro[i+1][j]:
    #                     while True:
    #                         gemas_validas = random.choice(cores_escolhidas)
    #                         if gemas_validas != tabuleiro[i][j]:
    #                             tabuleiro[i][j] == gemas_validas
    #                         break
    #                 if tabuleiro[i+3][j] == tabuleiro[i+4][j] and tabuleiro[i+3][j] == tabuleiro[i+5][j]:
    #                     while True:
    #                         gemas_validas = random.choice(cores_escolhidas)
    #                         if gemas_validas != tabuleiro[i+3][j]:
    #                             tabuleiro[i+3][j] == gemas_validas
    #                         break
    return(tabuleiro)

# Função que imprime o tabuleiro pronto na tela

def imprimir(tabuleiro, junt1, num_linhas):
    print()
    if num_linhas == 3:
        print("{}".format(NIVEL_FACIL))
        print("{}".format(LINHAFACIL))
    elif num_linhas == 6:
        print("{}".format(NIVEL_MEDIO))
        print("{}".format(LINHAMEDIO))
    elif num_linhas == 9:
        print("{}".format(NIVEL_DIFICIL))
        print("{}".format(LINHADIFICIL))
    for i in range(len(tabuleiro)):
        junt1 += "{} |".format(i)
        for j in range(len(tabuleiro[i])):
            junt1 += " {} ".format(tabuleiro[i][j])
        print(junt1.strip(), "|")
        junt1 = ""
    if num_linhas == 3:
        print("{}".format(LINHAFACIL))
        print("{}".format(NIVEL_FACIL))
    elif num_linhas == 6:
        print("{}".format(LINHAMEDIO))
        print("{}".format(NIVEL_MEDIO))
    elif num_linhas == 9:
        print("{}".format(LINHADIFICIL))
        print("{}".format(NIVEL_DIFICIL))