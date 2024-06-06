def main():
    T = int(input())
    competidores = list(map(int, input().split()))
    print(competidores.count(T))

if __name__ == "__main__":
    main()