
def Main():
    pontuacoes = {'1': 5, '2': 10, '3': 15, '4': 20, '5': 50}

    rodada = 1
    while True:
        jogador, jogadas = Entrada()

        pontuacao = [0, 0, 0]
        jogador_atual = (jogador - 1)

        for jogada in jogadas:
            if jogada == '0':
                jogador_atual = (jogador_atual + 1) % 3
                continue
            elif jogada == '-':
                vencedores = []
                for i in range(len(pontuacao)):
                    if pontuacao[i] == max(pontuacao):
                        vencedores.insert(i, i+1)

                print(f'RODADA {rodada}')
                if len(vencedores) == 1:
                    print(f'Ganhador com {max(pontuacao)} pontos')
                    print(f'Jogador {vencedores[0]}')
                elif len(vencedores) == 2:
                    print(f'Empate com {max(pontuacao)} pontos')
                    print(f'Jogador {vencedores[0]}, Jogador {vencedores[1]}')
                else:
                    print(f'Empate com {max(pontuacao)} pontos')
                    print(f'Jogador {vencedores[0]}, Jogador {vencedores[1]}, Jogador {vencedores[2]}')
                rodada += 1
                break
            else:
                pontuacao[jogador_atual] += pontuacoes[jogada]

def Entrada():
    jogador = int(input(""))
    jogadas = input("").replace(" ", "")
    return jogador, jogadas

Main()