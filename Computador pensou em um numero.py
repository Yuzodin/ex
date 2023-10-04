import random 
from time import sleep
pn= random. randint(0,5)
print('='*41)
print('Estou pensando em um numero entre 0 e 5..')
print('='*41)
print('Processando...')
sleep(2)
r= int(input ('Digite um numero entre 0 e 5: '))
if r == pn:
    print('Parabens você conseguiu me vencer. O numero era {}'.format (pn))
else:
    print('Ha, Ha, Ha ganhei pensei no numero {} não no {}'.format (pn,r))