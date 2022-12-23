# Principais constantes do nosso jogo

cores = {"azul": "\033[1;34m","vermelho": "\033[1;31m","roxo": "\033[1;35m","verde": "\033[1;32m","amarelo": "\033[1;33m","cinza": "\033[1;37m","limpa": "\033[m"}

cores_gemas = ['A','B','C','D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

MIN_TABULEIRO = 3
MAX_TABULEIRO = 10

MIN_CORES = 3
MAX_CORES = 26

INSTRUCOES = """
{}Instruções:{}
{}
- Inicialmente você irá informar a quantidade de linhas e colunas do seu tabuleiro
    -> Algumas opções: [Fácil: 3-6] [Médio: 6-8] [Difícil: 8-10];
- Você também irá determinar a quantidade de cores das gemas que vai querer no tabuleiro, tendo um limite de ser maior que 3 e menor ou igual a 26;
T - Para realizar as permutações, você vai precisar indicar a localização da linha e coluna dos dois elementos, que não podem ultrapassar o tamanho do tabuleiro;
D - Para obter dicas do jogo, porém você precisa saber que a cada dica pedida você perde um ponto;
I - Para rever as intruções do jogo;
TA - Para ver como o tabuleiro está no momento;
S - Para sair do jogo, vai ser informado pra você quantos pontos você conquistou.
{}
""".format(cores["vermelho"], cores["limpa"], cores["cinza"], cores["limpa"])

POWERUP4_COLUNAS = "{}Você formou um Power Up 4, toda a coluna da cadeia que foi formada no tabuleiro foi eliminada!{}".format(cores["azul"], cores["limpa"])

POWERUP4_LINHAS = "{}Você formou um Power Up 4, toda a linha da cadeia que foi formada no tabuleiro foi eliminada!{}".format(cores["azul"], cores["limpa"])

POWERUP5 = "{}Você formou um Power Up 5, todas as peças iguais a cadeia que foi formada no tabuleiro foram eliminadas!{}".format(cores["azul"], cores["limpa"])

