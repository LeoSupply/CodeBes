def main():
    n = int(input())
    inteiros = input().split()
    soma = 0
    for i in range(n):
        soma+=int(inteiros[i])
    print(soma)
if __name__ == "__main__":
    main()