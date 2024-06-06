def main():
    n = int(input())
    inteiros = input().split()
    lista_inteiros = [int(num) for num in inteiros]

    for i in range(n):
        if lista_inteiros[i] != 0:
            distancia = float('inf')
            for z in range(i+1, n):
                if lista_inteiros[z] == 0:
                    distancia = min(distancia, z - i)
                    break
            for z in range(i-1, -1, -1):
                if lista_inteiros[z] == 0:
                    distancia = min(distancia, i - z)
                    break
            if distancia>=9:
                print(9, end=' ')
            else:
                print(distancia, end=' ')
        else:
            print(0, end=' ')
        
if __name__ == "__main__":
    main()