# Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva
# todos os elementos exceto os elementos da diagonal secundária.

matriz = []
linhas = 4
colunas = 4
variavel = linhas + 1

# gerando matriz
for i in range (linhas):
    lista=[]
    for j in range(colunas):
        lista.append(input())
    matriz.append(lista)

for i,n in enumerate(matriz):
    for j,m in enumerate(n):
        # ajuste do índice da matriz, que começa em 1 e não em 0
        if j+i+2 == variavel:
            print(m,end=' ')