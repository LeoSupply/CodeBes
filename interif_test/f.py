jogador1= input('').upper()
jogador2 = input('').upper()

jogadas = {"PEDRA":0, "PAPEL":1, "TESOURA":2}
j1 = jogadas[jogador1]
j2 = jogadas[jogador2]

if j1 == j2:
    result = "Empate"
elif j1 == 0:
    if j2 == 1:
        result = "Jogador 2"
    elif j2 == 2:
        result = "Jogador 1"
elif j1 == 1:
    if j2 == 0:
        result = "Jogador 1"
    elif j2 == 2:
        result = "Jogador 2"
elif j1 == 2:
    if j2 == 0:
        result = "Jogador 2"
    elif j2 == 1:
        result = "Jogador 1"
print(result)