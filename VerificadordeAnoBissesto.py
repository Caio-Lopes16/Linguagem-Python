ano = int(input('Digite um ano: '))
if (ano % 4 == 0) or (ano % 400 == 0):
    print('O ano é bissesto!!')
elif (ano % 100 == 0):
    print('O ano NÃO é bissesto')
else:
    print('O ano NÃO é bissesto')
