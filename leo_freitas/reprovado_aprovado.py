def main():
    n1 = float(input())
    n2 = float(input())

    media = (n1*2 + n2*3)/5
    print('Aprovado' if media >= 7 else ('Reprovado' if media < 3 else 'Final'))

if __name__ == "__main__":
    main()
