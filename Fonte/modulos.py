# Funções genericas que vão estar presente no jogo

from constantes import *
import random

# Variáveis para as funções

tabuleiro = []
junt1 = ""

# Função que cria o tabuleiro com letras aleatorias do alfabeto que representam as cores das gemas

def criar(num_linhas, num_colunas, num_cores, tabuleiro):
    cores_escolhidas = []
    for x in range(num_cores):
        while True:
            op_cores = random.choice(cores_gemas)
            if op_cores not in cores_escolhidas:
                cores_escolhidas.append(op_cores)
                break
    for i in range(num_linhas):
    # verifica se logo na criação do tabuleiro são formadas cadeias de 3 elementos nas linhas
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

def validartroca(num_l1, num_c1, num_l2, num_c2, tabuleiro):
    # permutação na mesma linha
    if num_l1 == num_l2 and (num_c1 + 1) == num_c2 or num_c1 == num_l2 and (num_c1 - 1) == num_c2:
        return True
    # permutação na mesma coluna
    elif (num_l1 + 1) == num_l2 and num_c1 == num_c2 or (num_l1 - 1) == num_l2 and num_c1 == num_c2:
        return True
    else:
        return False

# realiza a troca de peças no tabuleiro

def trocar(num_l1, num_c1, num_l2, num_c2, tabuleiro):
    posinicial = tabuleiro[num_l1][num_c1]
    posfinal = tabuleiro[num_l2][num_c2]
    tabuleiro[num_l2][num_c2] = posinicial
    tabuleiro[num_l1][num_c1] = posfinal
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