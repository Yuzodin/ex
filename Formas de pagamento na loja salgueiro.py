print('='*19)
print('| LOJÃO SALGUEIRO |')
print('='*19)
pre= float(input ('Valor total da compra R$: '))
print('''Forma de pagamento:
      [1] À vista dinheiro/pix
      [2] No cartão de debito
      [3] 2X no cartão 
      [4] Mais vezes no cartão''')
op = int(input ('Qual a de pagamento?: '))
if op == 1:
   print('Sua compra de {} R$ com pagamento à vista sai por {:.2f} R$'.format(pre, pre - (pre*10/100)))
elif op == 2:
   print('Sua compra de {} R$ com pagamento no cartão de debito sai por {:.2f} R$'.format(pre, pre - (pre*5/100)))   
elif op == 3:
   print('Sua compra de {} R$ será parcelada em 2X de {:.2f} SEM JUROS'. format(pre, pre/2))  
elif op == 4:
   tp = int(input('Deseja dividir em quantas parcelas?: '))
   print('Sua compra de {} R$ será parcelada em {}X de COM JUROS DE 20% passará a custar: {:.2f} R$'.format(pre, tp, pre + (pre*20/100)))    
else:
   print('\033[31m OPÇÃO DE PAGAMENTO INVALIDA. TENTE NOVAMENTE \033[m')   