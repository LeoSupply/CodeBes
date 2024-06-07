def main():
    n = int(input())

    amigos = {}
    eventos = []
    nums = []  

    for _ in range(n):
        evento, num = input().split()

        eventos.append(evento)
        nums.append(num)

        if num not in amigos and evento == "R":
            amigos[num] = 0

        if evento == "T":
            atualiza = {chave: amigos[chave] + 5 for chave in amigos}
            amigos.update(atualiza)
        elif evento == "E":
            if num in amigos and "E" not in eventos[nums.index(num) + 1:]:
                amigos[num] = -1
        elif evento == "R":
            amigos[num] = 0

    amigos = dict(sorted(amigos.items()))
    for chave, valor in amigos.items():
        print(chave, valor)

if __name__ == "__main__":
    main()
