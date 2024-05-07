def main():
    N = int(input())
    jogadores = 0

    for _ in range(N):
        a = int(input())
        b = int(input())

        if (a * 5 - b * 3) > 40:
            jogadores+=1

    print(f'{jogadores}+' if jogadores == N else jogadores)

if __name__ == "__main__":
    main()
