def main():
    partidas = []
    while True:
        N = int(input())
        if N == 0:
            break

        j_par = input()
        j_impar = input()
        v_rodada = []
        for _ in range(N):
            j1, j2 = map(int, input().split())
            v_rodada.append(j_par if (j1 + j2) % 2 == 0 else j_impar)
        partidas.append(v_rodada)

    for i in range(len(partidas)):
        print('Teste', i+1)
        for jogador in partidas[i]:
            print(jogador)
        print()
                        
if __name__ == "__main__":
    main()