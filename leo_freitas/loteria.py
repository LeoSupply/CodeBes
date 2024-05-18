def main():
    jogo = list(map(int, input().split()))
    sorteado = list(map(int, input().split()))
    
    count = 0
    for num in jogo:
        if num in sorteado:
            count += 1

    acertos = {3:'terno', 
               4:'quadra', 
               5:'quina', 
               6:'sena'}
    
    if count < 3:
        print('azar')
    else:
        print(acertos[count])

if __name__ == "__main__":
    main()