# Definição da função para fazer o comparativo entre os números
def numeros_inteiros(numero_01, numero_02, numero_03):
    if numero_01 == numero_02 == numero_03:
        print('Todos os valores são iguais')
    elif numero_01 == numero_02 or numero_02 == numero_03 or numero_01 == numero_03:
        print('Existem dois valores iguais e um diferente')
    else:
        print('Todos os valores são diferentes')

# Definir as variáveis para importação dos dados do usuário
numero_01 = int(input())
numero_02 = int(input())
numero_03 = int(input())
condicao = numeros_inteiros(numero_01, numero_02, numero_03) 