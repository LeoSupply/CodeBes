def main():
    N = int(input())
    seq = list(map(int, input().split()))

    ocorrencias = {}

    min_num = float('inf')
    min_count = float('inf')

    for i in range(N):
        num = seq[i]
        if num not in ocorrencias:
            ocorrencias[num] = seq.count(num)

        if ocorrencias[num] < min_count or (ocorrencias[num] == min_count and num < min_num):
            min_count = ocorrencias[num]
            min_num = num
    
    print(min_num)
    
if __name__ == "__main__":
    main()