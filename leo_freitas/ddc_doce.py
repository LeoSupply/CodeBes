def main():
    N, K = map(int, input().split())
    sobras = []

    for _ in range(N):
        x, y = map(int, input().split())
        sobras.append(x % y)
    sobras = sorted(sobras)
    print(sobras[K - 1])

if __name__ == "__main__":
    main()