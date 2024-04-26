import math

def calculadora():
    print("--- Calculadora Avançada ---")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Exponenciação")
    print("6 - Raiz Quadrada")
    print("7 - Logaritmo")
    operacao = input("Escolha a operação desejada (1/2/3/4/5/6/7): ")

    if operacao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if operacao == '1':
            print("Resultado:", num1 + num2)
        elif operacao == '2':
            print("Resultado:", num1 - num2)
        elif operacao == '3':
            print("Resultado:", num1 * num2)
        elif operacao == '4':
            if num2 != 0:
                print("Resultado:", num1 / num2)
            else:
                print("Não é possível dividir por zero.")
    elif operacao == '5':
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        print("Resultado:", base ** expoente)
    elif operacao == '6':
        numero = float(input("Digite o número para calcular a raiz quadrada: "))
        print("Resultado:", round(math.sqrt(numero), 2))
    elif operacao == '7':
        numero = float(input("Digite o número para calcular o logaritmo: "))
        print("Resultado:", round(math.log(numero), 2))
    else:
        print("Opção inválida.")

calculadora()