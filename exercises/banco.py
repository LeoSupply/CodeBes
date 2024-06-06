def main():
    entrada = map(int, input().split())
    c, n = entrada

    caixas = [0]*c
    atrasos = 0
    for _ in range(n):
        d, t = map(int, input().split())

        caixa_livre = min(caixas)
        if max(0, caixa_livre - d) > 20:
            atrasos+=1

        caixas[caixas.index(caixa_livre)] = max(caixa_livre, d) + t

    print(atrasos)
    
if __name__ == "__main__":
    main()