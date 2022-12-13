# Funções genericas que vão estar presente no jogo

from constantes import *
import random

# Variáveis para as funções

tabuleiro = []
cores_escolhidas = []
junt1 = ""

# função que gera as cores a partir da quantidade escolhida pelo usuário

def criacores(num_cores, cores_escolhidas):
    for x in range(num_cores):
        while True:
            op_cores = random.choice(cores_gemas)
            if op_cores not in cores_escolhidas:
                cores_escolhidas.append(op_cores)
                break
    return(cores_escolhidas)

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

def criar(num_linhas, num_colunas, cores_escolhidas, tabuleiro):
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

# identificar cadeias horizontais e armazena indices de linhas e colunas das cadeias

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

# identificar cadeias verticais e armazena indices de linhas e colunas das cadeias

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
                            indices.append(j)
                            indices.append(fim)
                            indices.append(j)
                            cont = 1
                            cadeia_vertical.append(indices)
                    elif cont == 2:
                        cont = 1
            if len(cadeia_vertical) > 0:
                eliminaCadeia(tabuleiro, cadeia_vertical)

# elimina cadeia de elementos repetidos

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


# Função que imprime o tabuleiro pronto na tela

def imprimir(tabuleiro, junt1):
    print()
    linhas(tabuleiro)
    for i in range(len(tabuleiro)):
        junt1 += "{} |".format(i)
        for j in range(len(tabuleiro[i])):
            junt1 += " {} ".format(tabuleiro[i][j])
        print(junt1.strip(), "|")
        junt1 = ""
    linhas(tabuleiro, t=1)

# função que preenche o tabuleiro após a eliminação das peças

def preencher(tabuleiro, cores_escolhidas, trocas=0):
    gemaseliminadas = 0
    for i in range(len(tabuleiro)):
            for j in range(len(tabuleiro)):
                gemas_validas = random.choice(cores_escolhidas)
                if tabuleiro[i][j] == " ":
                    tabuleiro[i][j] = gemas_validas
                    gemaseliminadas+=1
    if trocas == 1:
        print("Você eliminou um total de {} gemas!".format(gemaseliminadas))
    return(gemaseliminadas)
