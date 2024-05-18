def main():
    N, M = map(int, input().split())

    acesas = list(map(int, input().split()))
    del acesas[0]

    for _ in range(N):
        lampadas = list(map(int, input().split()))
        if len(acesas) != 0:
            for i in range(1, lampadas[0]):
                if lampadas[i] not in acesas:
                    acesas.append(lampadas[i])
                elif lampadas[i] in acesas:
                    acesas.remove(lampadas[i])
        else:
            break
            
    print(acesas)
if __name__ == "__main__":
    main()