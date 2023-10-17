mai = 0
men = 0
for c in range(1,6):
    pe = float (input('Digite o peso da {}* pessoa: '.format (c)))
    if c == 1:
        mai = pe
        men = pe
    else:
        if pe > mai:
            mai = pe
        if pe < men:
            men = pe
print('O maior peso lido foi de: {}KG'.format(mai)) 
print('E o menor peso lido foi de: {}KG'. format(men))                   