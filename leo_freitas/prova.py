def main():
    notas = list(map(int, input().split()))
    
    soma = 0
    for _ in range(2):
        maior = max(notas)
        soma += maior
        notas.remove(maior)

    print(soma)
    
if __name__ == "__main__":
    main()