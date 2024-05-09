def main():
    N = int(input())
    K = int(input())
    
    soma = 0 
    for i in range(K + 1):
        soma += N * 10**i
    print(soma)

if __name__ == "__main__":
    main()