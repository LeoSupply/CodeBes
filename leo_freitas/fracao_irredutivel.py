def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    A, B, C, D = map(int, input().split())

    if B == D:
        dividendo = A + C
        divisor = B
    else:
        dividendo = (A * D) + (B * C)
        divisor = B * D

    mdc = gcd(dividendo, divisor)
    dividendo //= mdc
    divisor //= mdc

    print(dividendo, divisor)

if __name__ == "__main__":
    main()