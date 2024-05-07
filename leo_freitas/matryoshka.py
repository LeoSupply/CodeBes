def main():
    N = int(input())
    seq_ul = list(map(int, input().split()))
    seq_ol = sorted(seq_ul)
            
    count = 0
    bonecas = []
    for i in range(N):
        if seq_ol[i] != seq_ul[i]:
            count+=1
            bonecas.append(seq_ol[i])

    print(count)
    if count > 0:
        for i in range(len(bonecas)):
            print(bonecas[i], end=' ')

if __name__ == "__main__":
    main()