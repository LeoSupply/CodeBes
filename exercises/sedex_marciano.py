def main():
    L, A, P, R = map(int, input().split())
    diametro_base = (L**2 + P**2)**(1/2)
    diametro_cubo = (diametro_base**2 + A**2)**(1/2)
    diametro_cir = R*2

    if diametro_cubo <= diametro_cir:
        print('S')
    else:
        print('N')

if __name__ == "__main__":
    main()
