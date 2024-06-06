def main():
    ax, ay, bx, by = map(int, input().split())
    escalar = ax*bx + ay*by
    vetorial = ax*by - ay*bx
    print(escalar, vetorial)

if __name__ == "__main__":
    main()