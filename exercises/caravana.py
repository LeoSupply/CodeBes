def main():
    N = int(input())
    
    camelos = []
    for _ in range(N):
        P = int(input())
        camelos.append(P)
    
    media = sum(camelos) // N
    for i in range(N):
        print(media - camelos[i])

if __name__ == "__main__":
    main()