def main():
    N = int(input())
    
    e = []
    d = []

    for _ in range(N):
        M, L = input().split()
        if L == 'D':
            d.append(M)
        elif L == 'E':
            e.append(M)

    pares = 0
    for tam in e:
        if tam in d:
            d.remove(tam)
            pares+=1
    
    print(pares)

if __name__ == "__main__":
    main()