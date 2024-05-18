def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    count = 0
    for i in range(N):
        for j in range(M):
            if A[i] <= B[j]:
                count += 1 
    print(count)

if __name__ == "__main__":
    main()