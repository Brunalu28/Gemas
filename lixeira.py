
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


    # def criar(num_linhas, num_colunas, tabuleiro):
    # for i in range(num_linhas):
    #     tabuleiro.append([])
    #     for j in range(num_colunas):
    #             tabuleiro[i]
    # return(tabuleiro)

    # # completa o tabuleiro com letras aleatorias do alfabeto que representam as cores das gemas

    # def preencher(tabuleiro, num_cores):
    # cores_escolhidas = []
    # for x in range(num_cores):
    #     while True:
    #         op_cores = random.choice(cores_gemas)
    #         if op_cores not in cores_escolhidas:
    #             cores_escolhidas.append(op_cores)
    #             break
    # for i in range(len(tabuleiro)):
    #         for j in range(len(tabuleiro)):
    #             gemas_validas = random.choice(cores_escolhidas)
    #             if tabuleiro[i][j] == " ":
    #                 tabuleiro[i][j] = gemas_validas
    # return(tabuleiro)
