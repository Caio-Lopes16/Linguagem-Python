print('=====================================')
print('      CALCULADORA DE DESCONTOS       ')
print('=====================================')
print('')
valor = int(input('Digite um valor R$'))
desconto = float(input('Digite um desconto em % : '))
desconto = desconto/100
valor = valor-(valor*desconto)
print('O novo valor com o desconto será de R$', valor)