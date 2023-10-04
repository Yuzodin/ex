import random 
pn= random. randint(0,5)
r= int(input ('Digite um numero entre 0 e 5: '))
if r == pn:
    print('Parabens você acertou o numero que o computador pensou. O numero era {}'.format (pn))
else:
    print('Infelimente você não acertou o numero que o computador pensou. O numero era {}'.format (pn))