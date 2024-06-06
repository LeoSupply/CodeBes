def main():
    N = int(input())
    pares = list(map(int, input().split()))
    for i in range(2 * N - 1):
        if pares.count(pares[i]) != 2:
            print(pares[i])
            break

if __name__ == "__main__":
    main()