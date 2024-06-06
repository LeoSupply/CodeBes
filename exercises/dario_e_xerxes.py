def main():
    n = int(input())
    valores = [0,1,2,3,4]
    dario = 0
    xerxes = 0
    if n % 2 != 0 and n <= 999:
        for i in range(n):
            d, _, x = input()
            d = int(d)
            x = int(x)
            if 0<=d<=4 and 0<=x<=4:
                if (valores[d] + 1) % len(valores) == x or (valores[d] + 2) % len(valores) == x:
                    dario+=1
                elif (valores[x] + 1) % len(valores) == d or (valores[x] + 2) % len(valores) == d:
                    xerxes+=1

    if dario > xerxes:
        print('dario')
    else:
        print('xerxes')

if __name__ == "__main__":
    main()
