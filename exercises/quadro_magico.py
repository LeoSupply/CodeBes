def main():
    n = int(input())
    quadrado_magico = []

    for i in range(n):
        quadrado_magico.append(input().split())

    soma_linha = 0
    for i in range(n):
        soma_atual = 0
        for j in range(n):
            soma_atual+=int(quadrado_magico[i][j])

        if soma_linha == 0:
            soma_linha = soma_atual
        elif soma_atual != soma_linha:
            print(-1)
            return

    soma_coluna = 0
    for j in range(n):
        soma_atual = 0
        for i in range(n):
            soma_atual+=int(quadrado_magico[i][j])
        
        if soma_coluna == 0:
            soma_coluna = soma_atual
        elif soma_atual != soma_coluna:
            print(-1)
            return

    soma_diagonal_principal = 0
    soma_diagonal_secundaria = 0
    for i in range(n):
        soma_diagonal_principal += int(quadrado_magico[i][i])
        soma_diagonal_secundaria += int(quadrado_magico[i][(n-1)-i])

    if (soma_linha == soma_coluna == soma_diagonal_principal == soma_diagonal_secundaria):
        print(soma_linha)
    else:
        print(-1)
        
    
if __name__ == "__main__":
    main()
