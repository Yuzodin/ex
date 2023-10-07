from datetime import date
at= date.today().year
nas= int(input ('Digite o ano de nascimento do Atleta: '))
id= (at-nas)
print('Esse atleta tem {} anos de idade.'.format (id))
if id <= 9:
    print('Classificado como:\033[34m Mirin\033[m')
elif id > 9 and id <= 14:
    print('Classificado como:\033[36m Infantil\033[m') 
elif id > 14 and id <= 19:
    print('Classificado como:\033[33m Junior\033[m')  
elif id > 19 and id <= 25:
    print('Classificado como:\033[32m Sênior\033[m')
else: 
   print('Classificado como:\033[37m Senpai\033[m') 
           