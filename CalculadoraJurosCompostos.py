valorin = float(input('Digite o valor inicial: '))
taxajuros = float(input('Digite a taxa de juros anual: '))
anos = float(input('Digite o número de anos: '))
n = float(input('Quantos vezes os juros serão compostos por ano?: '))
taxajuros = taxajuros/100
print('O montante final é: ', round(valorin*(1+taxajuros/n)**(n*anos), 2))