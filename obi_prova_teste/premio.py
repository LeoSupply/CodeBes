def main():
    P = int(input())
    D = int(input())
    B = int(input())

    soma = P + (D * 2) + (B * 3)

    if soma >= 150:
        print("B")
    elif soma >= 120:
        print("D")
    elif soma >= 100:
        print("P")
    else:
        print("N")

if __name__ == "__main__":
    main()