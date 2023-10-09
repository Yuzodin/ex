peso= float(input('Dgite seu peso(km): '))
altura= float(input ('Digite sua altura(m): '))
imc = peso/(altura**2)
print('O seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Seu IMC está abaixo do recomendado para a sua altura.')
elif imc >= 18.5 and imc < 24.9:  
    print('Seu IMC é considerado normal para a sua altura.') 
elif imc >= 24.9 and imc < 30:
    print('Seu IMC está acima do recomendado para a sua altura.')    
elif imc > 30:
    print('Seu IMC está acima do recomendado para a sua altura.')