def main():
    N = int(input())
    seq = list(map(int, input().split()))

    soma = 0
    for i in range(N):
        soma += seq[i] - 1

    print(soma)

if __name__ == "__main__":
    main()