def main():
    N, M = map(int, input().split())
    caixas = []
    for i in range(M):
        x, y = map(int, input().split())
        if any(box[0] == x for box in caixas):
            caixas = [box for box in caixas if box[0] != x]
        caixas.append([x, y])
    caixas.sort()

    while len(caixas) < N:
        caixas.extend(caixas)
        
    for i in range(N):
        print(caixas[i][1])
        
if __name__ == "__main__":
    main()