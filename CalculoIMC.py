print('=====================================')
print(' CONVERSOR DE CELSIUS PARA FAREHEINT ')
print('=====================================')
print('')
peso = float(input('Digite o seu peso em kg: '))
altura =float(input('Digite a sua altura em cm: '))
imc=peso/(altura*altura)
imc=imc*10000
imc=round(imc, 2)
print('O seu IMC é: ', imc)
if imc < 18.5:
    print('Você está: Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Você está: Peso normal')
elif 25 <= imc < 30:
    print('Você está: Sobrepeso')
elif 30 <= imc < 35:
    print('Você está: Obeso')
else:
    print('Você está: Muito obeso')