def main():
    N = int(input())
    result = 1
    for _ in range(N):
        num, opr = input().split()
        num = int(num)
        if opr == '*':
            result *= num
        elif opr == '/':
            result /= num

    print(round(result))

if __name__ == "__main__":
    main()