nm= int(input ('Digite um numero: '))
print('''Escolha a opção da conversão:
[1] Conversão em binario.
[2] Coversão em octal.
[3] Conversão em hexadecimal''')
op= int(input ('Qual sera a base de conversão: '))
if op == 1:
    print ('O numero {} em binario é: {}'.format(nm,bin(nm)[2:]))
elif op == 2:
    print('O numero {} em octal é: {}'.format(nm,oct(nm)[2:]))
elif op == 3:
    print('O numero {} em hexadecimal é: {}'.format(nm,hex(nm)[2:]))  
else:
    print('Opção não encontrada tente novamente! ')      