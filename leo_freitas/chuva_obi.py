def main():
    N = int(input())
    S = int(input())
    X = list(map(int, input().split()))

    count = 0
    soma_acumulada = {0: 1}

    soma = 0
    for i in range(N):
        soma += X[i]
        count += soma_acumulada.get(soma - S, 0)
        soma_acumulada[soma] = soma_acumulada.get(soma, 0) + 1

    print(count)

if __name__ == "__main__":
    main()
