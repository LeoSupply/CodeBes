def main():
    vencedores = []
    while True:
        R = int(input())
        if R == 0:
            break

        pontos_a = 0
        pontos_b = 0
        for _ in range(R):
            A, B = map(int, input().split())
            pontos_a += A
            pontos_b += B
        
        vencedores.append('Aldo' if pontos_a > pontos_b else 'Beto')
    for i in range(1, len(vencedores) + 1):
        print(f'Teste {i}\n{vencedores[i-1]}\n')

if __name__ == "__main__":
    main()