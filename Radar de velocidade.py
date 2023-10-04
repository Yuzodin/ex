Radar= int(input ('Qual a velocidade do carro pego pelo radar: '))
if Radar > 80:
    print('\033[31m Você foi MULTADO em {}R$ por dirigir acima do limite de velocidade de 80km/h\033[m '.format ((Radar-80)*7))
    print('7,00 R$ para cada Km acima do Limite')
    print('\033[32m Tenha um bom dia! Dirija com segurança\033[m')
else:
    print('\033[32m Tenha um bom dia! Dirija com segurança\033[m')    