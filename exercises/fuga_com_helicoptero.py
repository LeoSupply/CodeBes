def main():
    H, P, F, D = map(int, input().split())

    for _ in range(16):
        if D == -1:
            F = (F-1) % 16
        elif D == 1:
            F= (F+1) % 16
        
        if F == H:
            print('S')
            return
        elif F == P:
            print('N')
            return

if __name__ == "__main__":
    main()