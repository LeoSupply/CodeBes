def main():
    n = int(input())
    count = 0
    for _ in range(n):
        l, c = map(int, input().split())
        if l>c:
            count+=c
    print(count)
    
if __name__ == "__main__":
    main()