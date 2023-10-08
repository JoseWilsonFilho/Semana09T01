def operacoes(valor_01, valor_02, operacao):
    if operacao == 1:
        adicao = valor_01 + valor_02
        print(f'{adicao}')
    elif operacao == 2:
        subtracao = valor_01 - valor_02
        print(f'{subtracao}')
    elif operacao == 3:
        multiplicacao = valor_01 * valor_02
        print(f'{multiplicacao}')
    elif operacao == 4:
        divisao = valor_01 / valor_02
        print(f'{divisao:.2f}')
    else:
        return ValueError
    
valor_01 = int(input())
valor_02 = int(input())
operacao = int(input())
resultados = operacoes(valor_01, valor_02, operacao)

