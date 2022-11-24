from constantes import *
from funções import *

print("-=-" * 30)
print("-=-" * 30)
print("-=-" * 11, "BEM VINDO AO GEMAS!","-=-" * 12)
print("-=-" * 30)
print("-=-" * 30)

while True:
    num_linhas = int(input("Digite a quantidade de linhas do tabuleiro [3-10]: "))
    if num_linhas >= 3 and num_linhas <= 10:
        while True:
            num_colunas = int(input("Digite a quantidade de colunas do tabuleiro [3-10]: "))
            if num_colunas >= 3 and num_colunas <= 10:
                while True:
                    num_cores = int(input("Digite a quantidade de cores de gemas que você deseja [3-26]: "))
                    if num_cores >= 3 and num_cores <= 26:
                        criar(num_linhas, num_colunas, num_cores)
                        print(imprimir(tabuleiro, junt1))
                        break
                    else:
                        print("Digite um valor entre 3 e 26")
                break
            else:
                print("Digite um valor entre 3 e 10")
                pass
        break
    else:
        print("Digite um valor entre 3 e 10")
        pass


