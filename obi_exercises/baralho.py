def main():
    entrada = input()
    baralho = {'C':13,'E':13,'U':13,'P':13}
    for i in range(0 , len(entrada), 3):
        carta = entrada[i:i+3]
        naipe = carta[2]
        if entrada.count(carta) != 1:
            baralho[naipe] = 'erro'
        else:
            if not isinstance(baralho[naipe], str):
                baralho[naipe] -= 1
    for valor in baralho.values():
        print(valor)

if __name__ == "__main__":
    main()