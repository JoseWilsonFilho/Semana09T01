def definir_tarefa(numero, resto_divisao):
    if (resto_divisao == 0):
        return ((9 * numero) + 7)
    
    elif (resto_divisao == 1):
        if (numero % 2 == 0):
            return 'par'
        else:
            return 'ímpar'
        
    elif (resto_divisao == 2):
        return ((5 * numero ** 2) - (3 * numero) + 42)
    
    elif (resto_divisao == 3):
        return (numero // 10)
    
    elif (resto_divisao == 4):
        return (numero ** 2)

def main():
    numero = input().strip()
    numero = int(numero)

    resto_divisao = numero % 5

    resultado = definir_tarefa(numero, resto_divisao)

    print(resultado)

if __name__ == '__main__':
    main()