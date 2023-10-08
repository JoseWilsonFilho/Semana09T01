def quadrado(lado_01, lado_02):
    if lado_01 == lado_02:
        print('QUADRADO')
    elif lado_01 != lado_02:
        perimetro = 2*lado_01 + 2*lado_02
        area = lado_01 * lado_02
        print(f'{perimetro} - {area}')

lado_01 = int(input())
lado_02 = int(input())
resultado = quadrado(lado_01, lado_02)

