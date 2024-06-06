def main():
    N = int(input())
    x, operador, y = input().split()
    x, y = int(x), int(y)

    if operador == '+':
        if x+y > N:
            print('OVERFLOW')
        else:
            print('OK')
    elif operador == '*':
        if x*y > N:
            print('OVERFLOW')
        else:
            print('OK')

if __name__ == "__main__":
    main()
