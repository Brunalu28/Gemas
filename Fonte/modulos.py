# Funções genericas que vão estar presente no jogo

from os import system, name
from constantes import *
import random

# função para limpar o terminal

def limpaTela():
    # windows
    if name == 'nt':
      system('cls')
    # mac e linux
    else:
      system('clear')

# função que gera as cores a partir da quantidade escolhida pelo usuário no início do jogo

def criacores(num_cores):
    cores_escolhidas = []
    for x in range(num_cores):
        while True:
            op_cores = random.choice(cores_gemas)
            if op_cores not in cores_escolhidas:
                cores_escolhidas.append(op_cores)
                break
    return(cores_escolhidas)


# cria a apresentação do tabuleiro com linhas ao redor

def linhas(tabuleiro, t=0):
    tam = len(tabuleiro)
    l = "  +"
    j = "   "
    if t == 0:
        for i in range(len(tabuleiro)):
            j += " {} ".format(i)
        print(j)
        for i in range(len(tabuleiro)):
            l += "{}".format("---")
            if i == tam - 1:
                l += "{}".format("+")
        print(l)
    elif t == 1:
        for i in range(len(tabuleiro)):
            l += "{}".format("---")
            if i == tam - 1:
                l += "{}".format("+")
        print(l)
        for i in range(len(tabuleiro)):
            j += " {} ".format(i)
        print(j)


# Função que cria o tabuleiro com letras aleatorias do alfabeto que representam as cores das gemas

def criar(num_linhas, num_colunas, cores_escolhidas):
    tabuleiro = []
    for i in range(num_linhas):
    # verifica se logo na criação do tabuleiro são formadas cadeias de 3 elementos nas linhas, evitando a criação do tabuleiro já com cadeias formadas nas linhas
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
    return(tabuleiro)

# valida a troca permitindo que só sejam feitas se as gemas estiverem lado a lado ou uma abaixo da outra

def validartroca(num_l1, num_c1, num_l2, num_c2):
    # permutação na mesma linha
    if (num_l1 == num_l2 and (num_c1 + 1) == num_c2) or (num_l1 == num_l2 and (num_c1 - 1) == num_c2):
        return True
    # permutação na mesma coluna
    elif ((num_l1 + 1) == num_l2 and num_c1 == num_c2) or ((num_l1 - 1) == num_l2 and num_c1 == num_c2):
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

# identifica cadeias de 3 elementos na horizontal e armazena indices das linhas das cadeias

def cadeiasHorizontais(tabuleiro):
    for i in range(len(tabuleiro)):
            cadeia_horizontal = []
            inicio = ""
            fim = ""
            cont = 1
            indices = []
            for j in range(len(tabuleiro)):
                if j < len(tabuleiro) - 1:
                    if tabuleiro[i][j] == tabuleiro[i][j + 1]:
                        cont += 1
                        if cont >= 3:
                            inicio = ((j + 2) - cont)
                            fim = (j + 1)
                            indices.append(i)
                            indices.append(inicio)
                            indices.append(i)
                            indices.append(fim)
                            cont = 1
                            cadeia_horizontal.append(indices)
                    elif cont == 2:
                        cont = 1
            if len(cadeia_horizontal) > 0:
                eliminaCadeia(tabuleiro, cadeia_horizontal)

# identifica cadeias com 3 elementos na vertical e armazena indices das colunas das cadeias

def cadeiasVerticais(tabuleiro):
    for i in range(len(tabuleiro)):
            cadeia_vertical = []
            inicio = ""
            fim = ""
            cont = 1
            indices = []
            for j in range(len(tabuleiro)):
                if j < len(tabuleiro) - 1:
                    if tabuleiro[j][i] == tabuleiro[j + 1][i]:
                        cont += 1
                        if cont >= 3:
                            inicio = ((j + 2) - cont)
                            fim = (j + 1)
                            indices.append(inicio)
                            indices.append(i)
                            indices.append(fim)
                            indices.append(i)
                            cont = 1
                            cadeia_vertical.append(indices)
                    elif cont == 2:
                        cont = 1
            if len(cadeia_vertical) > 0:
                eliminaCadeia(tabuleiro, cadeia_vertical)

# elimina cadeia de 3 elementos repetidos por meio dos indices indicados pela função de verificar cadeias horizontais e verticais

def eliminaCadeia(tabuleiro, cadeia):
    li = 0
    lf = 0
    ci = 0
    cf = 0
    for i in range(len(cadeia)):
        for j in range(len(cadeia[i])):
            li = cadeia[i][0]
            lf = cadeia[i][2]
            ci = cadeia[i][1]
            cf = cadeia[i][3]
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if i >= li and j >= ci and i <= lf and j <= cf:
                tabuleiro[i][j] = " "


# função que imprime o tabuleiro pronto na tela

def imprimir(tabuleiro):
    junt1 = ""
    print()
    linhas(tabuleiro)
    for i in range(len(tabuleiro)):
        junt1 += "{} |".format(i)
        for j in range(len(tabuleiro[i])):
            if j == (len(tabuleiro) - 1):
                junt1 += " {}".format(tabuleiro[i][j])
            else:
                junt1 += " {} ".format(tabuleiro[i][j])
        print(junt1, "|")
        junt1 = ""
    linhas(tabuleiro, t=1)

# função que contabiliza os pontos em cada rodada de trocas

def peçasEliminadas(tabuleiro):
    gemaseliminadas = 0
    contgemas = 0
    for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)):
                if tabuleiro[i][j] == " ":
                    contgemas +=1
    gemaseliminadas = contgemas
    contgemas = 0
    return(gemaseliminadas)


# função que preenche o tabuleiro após a eliminação das peças

# preenche com novas gemas da mesma lista de cores escolhidas pelo usuário ao início do jogo

def preencher(tabuleiro, cores_escolhidas, num_cores):
    for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)):
                n = random.randrange(0, num_cores - 1)
                if tabuleiro[i][j] == " ":
                    tabuleiro[i][j] = cores_escolhidas[n]


# função deslocar (desloca todos os elementos para baixo após a eliminação das cadeias)

def deslocarElementos(tabuleiro, coordenadas):
    for i in range(len(tabuleiro) + 1):
        if i == coordenadas:
            contvazios = 0
            for j in range(len(tabuleiro)):
                if j +1 < len(tabuleiro):
                    if tabuleiro[j][i] == " " and tabuleiro[j+1][i] != " ":
                        contvazios +=1
    while contvazios > 0:
        for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)):
                if j +1 < len(tabuleiro):
                    if tabuleiro[j][i] != " " and tabuleiro[j+1][i] == " ":
                        tabuleiro[j+1][i] = tabuleiro[j][i]
                        tabuleiro[j][i] = " "
        contvazios -= 1

# função auxiliar para deslocar

def desloca(tabuleiro):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[j][i] == " ":
                deslocarElementos(tabuleiro, j)
    return(tabuleiro)


# função power up 4 e 5 linhas e colunas que identificam as linhas e colunas

def powerup4e5_linhas(tabuleiro):
    for i in range(len(tabuleiro)):
            indicesPU5 = []
            indicesPU4 = []
            cont = 1
            for j in range(len(tabuleiro)):
                if j < len(tabuleiro) - 1:
                    if tabuleiro[i][j] == tabuleiro[i][j + 1]:
                        cont += 1
                        if cont >= 5:
                            if tabuleiro[i][j] != " ":
                                indicesPU5.append(tabuleiro[i][j])
                                cont = 1
                    elif cont == 4:
                        indicesPU4.append(i)
                        cont = 1
                    elif cont == 2 or cont == 3:
                        cont = 1
            if len(indicesPU5) > 0:
                eliminapowerup5(tabuleiro, indicesPU5)
            if len(indicesPU4) > 0:
                eliminapowerup4_linhas(tabuleiro, indicesPU4)

def powerup4e5_colunas(tabuleiro):
    for i in range(len(tabuleiro)):
            indicesPU5 = []
            indicesPU4 = []
            cont = 1
            for j in range(len(tabuleiro)):
                if j < len(tabuleiro) - 1:
                    if tabuleiro[j][i] == tabuleiro[j + 1][i]:
                        cont += 1
                        if cont >= 5:
                            if tabuleiro[i][j] != " ":
                                indicesPU5.append(tabuleiro[j][i])
                                cont = 1
                    elif cont == 4:
                        indicesPU4.append(i)
                        cont = 1
                    elif cont == 2 or cont == 3:
                        cont = 1
            if len(indicesPU5) > 0:
                eliminapowerup5(tabuleiro, indicesPU5)
            if len(indicesPU4) > 0:
                eliminapowerup4_colunas(tabuleiro, indicesPU4)

# funções auxiliares que eliminam os power ups

# exclui a linha

def eliminapowerup4_linhas(tabuleiro, indices):
    for i in range(len(tabuleiro)):
        if i == indices[0]:
            for j in range(len(tabuleiro[i])):
                tabuleiro[i][j] = " "
    print(POWERUP4_LINHAS)

# exclui a coluna

def eliminapowerup4_colunas(tabuleiro, indices):
    for i in range(len(tabuleiro)):
        if i == indices[0]:
            for j in range(len(tabuleiro[i])):
                tabuleiro[j][i] = " "
    print(POWERUP4_COLUNAS)

# exclui todas as letras iguais as letras que formaram a cadeia com 5 elementos

def eliminapowerup5(tabuleiro, indices):
    for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)):
               if tabuleiro[i][j] == indices[0]:
                   tabuleiro[i][j] = " "
    print(POWERUP5)

# função para dar dicas do jogo

# obs - diferente da função do roteiro, foram identificadas dicas do jogo referentes a linha e coluna do tabuleiro, 
# basicamente se possuirem duas gemas iguais e a quarta gema for igual as duas anteriores ele informa o indice da linha 
# e coluna da quarta gema, ex. AABA, será informado os indices da ultima gema A, tanto em casos na linha como na coluna.

# dá dicas de jogadas nas linhas

def dicasdojogo_horizontal(tabuleiro):
    contvazios = 0
    for i in range(len(tabuleiro)):
        cont = 1
        indices_dicas = []
        for j in range(len(tabuleiro)):
            if j < len(tabuleiro) - 1:
                if tabuleiro[i][j] == tabuleiro[i][j + 1]:
                    cont += 1
                    if cont >= 2:
                        if j < len(tabuleiro) - 3:
                            if tabuleiro[i][j+3] == tabuleiro[i][j]:
                                indices_dicas.append([i, j+3])
                                cont = 1
                elif cont == 2:
                    cont = 1
        if len(indices_dicas) > 0:
            for i in range(len(indices_dicas)):
                print("{}Linha e coluna do elemento que forma uma cadeia na horizontal: {}{}".format(cores["verde"], indices_dicas[i], cores["limpa"]))
        else:
            contvazios +=1
    if contvazios > 0:
        print("{}Não temos mais combinações aparentes nas linhas! {}{}".format(cores["vermelho"], [-1, -1], cores["limpa"]))

# dá dicas de jogadas nas colunas

def dicasdojogo_vertical(tabuleiro):
    contvazios = 0
    for i in range(len(tabuleiro)):
        cont = 1
        indices_dicas = []
        for j in range(len(tabuleiro)):
            if j < len(tabuleiro) - 1:
                if tabuleiro[j][i] == tabuleiro[j + 1][i]:
                    cont += 1
                    if cont >= 2:
                        if j < len(tabuleiro) - 3:
                            if tabuleiro[j+3][i] == tabuleiro[j][i]:
                                indices_dicas.append([j+3, i])
                                cont = 1
                elif cont == 2:
                    cont = 1
        if len(indices_dicas) > 0:
            for i in range(len(indices_dicas)):
                print("{}Linha e coluna do elemento que forma uma cadeia na vertical: {}{}".format(cores["verde"], indices_dicas[i], cores["limpa"]))
        else:
            contvazios +=1
    if contvazios > 0:
        print("{}Não temos mais combinações aparentes nas colunas! {}{}".format(cores["vermelho"], [-1, -1], cores["limpa"]))
