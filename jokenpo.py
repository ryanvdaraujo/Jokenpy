from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('~~' * 12)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('~~' * 12)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('O Jogador VENCEU!')
    elif jogador == 2:
        print('O computador VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('O computador VENCEU!') 
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('O Jogador VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
else:
    if jogador == 0:
        print('O jogador VENCEU!') 
    elif jogador == 1:
        print('O computador VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
