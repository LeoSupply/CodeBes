def main():
    N = int(input())
    d = 0
    for _ in range(N):
        v, t = map(int, input().split())
        d += v * t
    print(d)
if __name__ == "__main__":
    main()