def main():
    N, Q = map(int, input().split())
    seq = list(map(int, input().split()))

    min_count = []
    for _ in range(Q):
        L, R = map(int, input().split())

        ocorrencia = {}
        for i in range(L - 1, R):
            if seq[i] not in ocorrencia:
                ocorrencia[seq[i]] = 0
            ocorrencia[seq[i]] += 1

        min_count.append(max(ocorrencia.values()))

    for num in min_count:
        print(num)

if __name__ == "__main__":
    main()
    