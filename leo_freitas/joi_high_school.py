def main():
    N = int(input())
    K = int(input())
    S = input()

    if S.count('R') == K:
        print('W')
    elif S.count('W') == N - K:
        print('R')

if __name__ == "__main__":
    main()