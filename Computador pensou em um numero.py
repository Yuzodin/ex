tenta = 0
import random 
from time import sleep
pc= random. randint(0,10)
print('='*41)
print('Estou pensando em um numero entre 0 e 10..')
print('='*41)
print('Processando...')
sleep(2)
acertou = False
while not acertou:
    player = int(input ('Tente acertar o numero que o computador pensou!! Digite um numero entre 0 e 10: '))
    tenta += 1
    if player == pc:
        acertou = True
        print('Parabens você conseguiu vencer o computador. O numero era {}'.format (pc))
        print('Foram necessarias: {} tentativas para acertar'.format(tenta))  
    else:
        if player < pc:
            print('O numero que pensei é maior... Tente novamnete: ')
        else:
            print('O numero que pensei é menor... Tente  novamente: ')    
    
