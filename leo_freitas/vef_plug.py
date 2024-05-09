def main():
    plug_a = list(map(int, input().split()))
    plug_b = list(map(int, input().split()))

    compativel = True
    for i in range(5):
        if plug_a[i] == plug_b[i]:
            compativel = False
            break
        
    print('Y' if compativel else 'N')

if __name__ == "__main__":
    main()