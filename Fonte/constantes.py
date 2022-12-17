import sys
# Principais constantes do nosso jogo

gemascoloridas = {"AZUL": "\033[34m", "BRANCO": "\033[37m", "CIANETO": "\033[36m", "AMARELO": "\033[33m", "MAGENTA": "\033[35m", "VERDE": "\033[32m", "VERMELHO": "\033[31m",}

cores_gemas = ['A','B','C','D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

MIN_TABULEIRO = 3
MAX_TABULEIRO = 10

MIN_CORES = 3
MAX_CORES = 26

INSTRUCOES = """

ALGUNS AVISOS IMPORTANTES PARA O JOGO:

T - PARA REALIZAR A TROCA DE GEMAS;
D - PARA DICAS NO JOGO (PERDE 1 PONTO);
S - PARA SAIR DO JOGO.

"""


