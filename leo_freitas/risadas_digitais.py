def main():
    risada = input()
    vogais = "aeiou"
    risada_vogais = ''
    for char in risada:
        if char in vogais:
            risada_vogais+=char

    for i in range(1, len(risada_vogais) + 1):
        if risada_vogais[i-1] != risada_vogais[-i]:
            print('N')
            return
    print('S')
if __name__ == "__main__":
    main()