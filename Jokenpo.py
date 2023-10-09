from random import randint
from time import sleep
acao = ('Pedra', 'Papel', 'Tesoura', 'Se Confundir')
cpu= randint (0,2)
print(''' Suas opções de jogada
      [0] Pedra
      [1] Papel
      [2} Tesoura ''')
player= int(input('Qual sua jogada?: '))
print('\033[34m JO \033[m')
sleep(1)
print('\033[31m KEN \033[m')
sleep(1)
print ('\033[37m PO!!! \033[m')
print('\033[35m -\033[m'*14)
print('O computador escolheu: {}'.format (acao[cpu]))
print('O player escolheu: {}'.format(acao[player]))
print('\033[34m -\033[m'*14)
if cpu == 0:
    if player == 0:
        print('\033[32m EMPATE \033[m')
    elif player == 1:
        print('\033[33m VITORIA DO PLAYER!. \033[m')
    elif player == 2:  
        print('\033[135m VITORIA DO COMPUTADOR!. \033[m')
    else:
        print('\033[31m O player se confundiu é não jogou nada \033[m')       

elif cpu == 1:
    if player == 0:
        print('\033[135m VITORIA DO COMPUTADOR!. \033[m')
    elif player == 1:
        print('\033[32m EMPATE \033[m')
    elif player == 2:  
        print('\033[33m VITORIA DO PLAYER!. \033[m')
    else:
        print('\033[31m O player se confundiu é não jogou nada \033[m')   
    
elif cpu == 2:
    if player == 0:
        print('\033[33m VITORIA DO PLAYER!. \033[m')
    elif player == 1:
        print('\033[35m VITORIA DO COMPUTADOR!. \033[m')
    elif player == 2:  
        print('\033[32m EMPATE \033[m')
    else:
        print('\033[31m O player se confundiu é não jogou nada \033[m')  