def main():
    n = int(input())
    entrada = input().replace(' ', '')

    a = False
    b = False

    for i in range(n):
        if entrada[i] == '1':
            a = not a
        elif entrada[i] == '2':
            a = not a
            b = not b

    print(int(a))
    print(int(b))


if __name__ == "__main__":
    main()
