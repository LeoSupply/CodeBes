def main():
    N, M = map(int, input().split())
    distancias = list(map(int, input().split()))
    possibilidades = [[distancias[i], M - distancias[i]] for i in range(N)]

    n = min(possibilidades[0])
    soma = min(possibilidades[0])
    for i in range(1, len(possibilidades)):
        n = min(possibilidades[i]) if min(possibilidades[i]) >= n else (max(possibilidades[i]) if max(possibilidades[i]) >= n else -1)
        soma+=n
        if n == -1:
            print(n)
            return
        
    print(soma)

if __name__ == "__main__":
    main()