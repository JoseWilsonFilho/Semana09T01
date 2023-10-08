def menor(numero_01, numero_02, numero_03):
    if(abs(numero_01 - numero_02) <= abs(numero_01 - numero_03)):
        return numero_01 - numero_02
    elif(abs(numero_01 - numero_02) >= abs(numero_01 - numero_03)):
        return numero_01 - numero_03
    else:
        raise ValueError('Inválido!')

numero_01 = input().strip() 
numero_02 = input().strip()
numero_03 = input().strip()

numero_01 = int(numero_01) 
numero_02 = int(numero_02)
numero_03 = int(numero_03)

qual_menor = menor(numero_01, numero_02, numero_03)
print(f'{abs(qual_menor)}')
