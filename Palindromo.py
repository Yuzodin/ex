f = str (input ('Escreva uma frase: ')).strip(). upper()
p = f.split()
j = ''. join(p)
print('Você escreveu a seguinte frase: {}'.format (j))
inv = ''
for letra in range(len(j) -1, -1, -1):
    inv += j[letra]
print('Seu inverso é : {}'. format (inv))    
if inv == j:
    print('Esta frase é um palindromo!. ')
else:
    print('Essa frase nâo é um palindromo. ')   
