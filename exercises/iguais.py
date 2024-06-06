def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    soma = sum(A) + X
    if soma % N == 0:
        result = 'Boa Sorte'
    else:
        result = 'Sem Sorte'
    print(result)

if __name__ == "__main__":
    main()