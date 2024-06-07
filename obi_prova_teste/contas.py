def main():
    V = int(input())
    contas = sorted([int(input()) for _ in range(3)])

    total = 0
    i = 0
    for conta in contas:
        if (total + conta) <= V:
            total += conta
            i += 1
        else:
            break

    print(i)

if __name__ == "__main__":
    main()