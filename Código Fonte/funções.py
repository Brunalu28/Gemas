# Funções genericas que vão estar presente no jogo

# from main import *
from constantes import *
import random

# Função que cria o tabuleiro comletras aleatorias do alfabeto que representam as cores das gemas

def criar(num_linhas, num_colunas, num_cores):
    for x in range(num_cores):
        op_cores = random.choice(cores_gemas)
        cores_escolhidas.append(op_cores)
    for i in range(num_linhas):
        linhas = []
        for j in range(num_colunas):
            linhas.append(random.choice(cores_escolhidas))
        tabuleiro.append(linhas)
    return(tabuleiro)

# Função que imprime o tabuleiro pronto na tela

def imprimir(tabuleiro, junt1):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            junt1 += "{} ".format(tabuleiro[i][j])
        print(junt1)
        if i+1 == len(tabuleiro) and j+1 == len(tabuleiro[i]):
            return(junt1.strip())
        junt1 = ""