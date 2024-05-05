def main():
    n = int(input())
    entrada = input().split()

    max_contagem = 1  
    contagem_atual = 1

    for i in range(1, n):
        if entrada[i] == entrada[i - 1]:
            contagem_atual += 1
            max_contagem = max(max_contagem, contagem_atual)
        else:
            contagem_atual = 1

    print(max_contagem)

if __name__ == "__main__":
    main()
