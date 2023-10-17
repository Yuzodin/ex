soma = 0
maior = 0
nomemaior = ''
tot20 = 0
for c in range(1, 5):
    print('------ {} Pessoa ------'.format(c))
    nome = str (input('Nome: '))
    idade = int(input ('Idade: '))
    Sexo = str(input ('Sexo [M/F]: ')).strip()
    soma += idade
    if idade == 1 and Sexo in 'Mm':
        maior = idade
        nomemaior = nome
    if Sexo in 'Mm' and idade > maior:
            maior = idade
            nomemaior = nome
    if Sexo in 'Ff' and idade <= 20:
            tot20 += 1     
media = soma/4
print('A media de idade das pessoas é de: {}'.format(media))
print('O homen mais velho é {} com {} de idade'.format(nomemaior, maior))
print('Ao todo são {} mulheres com menos de 20 anos'.format(tot20))
    
    

