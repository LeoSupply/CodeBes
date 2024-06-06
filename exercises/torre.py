def main():
    n = int(input())
    matriz = []
    for _ in range(n):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    soma_linhas = [sum(linha) for linha in matriz]
    soma_colunas = [sum(matriz[i][j] for i in range(n)) for j in range(n)]

    peso_max = 0
    for i in range(n):
        for j in range(n):
            soma_linha = soma_linhas[i] - matriz[i][j]
            soma_coluna = soma_colunas[j] - matriz[i][j]
            peso_max = max(peso_max, soma_linha + soma_coluna)
    print(peso_max)

if __name__ == "__main__":
    main()