def main():
    sorteados = []
    while True:
        N = int(input())
        if not N:
            break
        
        entrada = list(map(int, input().split()))
        for i in range(N):
            if entrada[i] == i + 1:
                sorteados.append(entrada[i])
                break

    for i in range(len(sorteados)):
        print(f'Teste {i + 1}\n{sorteados[i]}\n')

if __name__ == "__main__":
    main()