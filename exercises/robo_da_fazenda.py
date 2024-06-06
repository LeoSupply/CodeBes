def main():
    N, C, S = map(int, input().split())
    seq = list(map(int, input().split()))

    posicao = 0
    count = 0
    for i in range(C):
        if posicao == (S-1):
            count+=1
        posicao = (posicao + (seq[i])) % N
        
    if posicao == (S-1):
            count+=1

    print(count)

if __name__ == "__main__":
    main()
