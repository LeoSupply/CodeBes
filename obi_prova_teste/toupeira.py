def main():
    nos, arestas = map(int, input().split())

    grafos = {tuple(map(int, input().split())) for _ in range(arestas)}

    sugestoes = int(input())
    soma = 0

    for _ in range(sugestoes):
        sugestao = list(map(int, input().split()))
        existe = True
        for i in range(1, sugestao[0]):
            if (sugestao[i], sugestao[i+1]) not in grafos and (sugestao[i+1], sugestao[i]) not in grafos:
                existe = False
                break
        if existe:
            soma += 1

    print(soma)

if __name__ == "__main__":
    main()
