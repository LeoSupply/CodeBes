def main():
    N = int(input())

    a, b = 1, 0
    for _ in range(N):
        a, b = a+b, a
        
    print(a)

if __name__ == "__main__":
    main()
