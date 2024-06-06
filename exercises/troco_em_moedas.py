def main():
    c = int(input())
    moedas = {100: 0, 50: 0, 25: 0, 10: 0, 5: 0, 1: 0}

    for valor, quantidade in moedas.items():
        if c >= valor:
            moedas[valor] = c // valor
            c -= moedas[valor] * valor

    quantidade = sum(moedas.values())

    print(quantidade)
    for valor in moedas.values():
        print(valor)


if __name__ == "__main__":
    main()
