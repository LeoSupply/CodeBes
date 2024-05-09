def main():
    N = int(input())
    valores_a = list(map(int, input().split()))
    M = int(input())
    valores_b = list(map(int, input().split()))

    pontos = 0
    for valor in valores_a:
        pontos += valor
        if pontos in valores_b:
            pontos = 0

    print(pontos)
if __name__ == "__main__":
    main()