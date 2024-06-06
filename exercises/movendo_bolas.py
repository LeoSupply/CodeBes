def main():
    N, M = map(int, input().split())
    bolas = {}
    for _ in range(M):
        x, y = map(int, input().split())
        bolas[x] = y
    bolas = dict(sorted(bolas.items()))

    count = 0
    while count < N:
        for valor in bolas.values():
            print(valor)
            count += 1
            if count >= N:
                break

if __name__ == "__main__":
    main()