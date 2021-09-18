def defineFormato(lado1, lado2, lado3):
    if (lado1 <= 0 ) or (lado2 <= 0 ) or (lado3 <= 0 ):
        return 'Não é um triângulo'

    if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
        return 'Não é um triângulo'
    elif (lado1 == lado2) and (lado1 == lado3):
        return 'Equilátero'
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        return 'Isósceles'
    else :
        return 'Escaleno'

def imagemDoFormato(formato):
    if formato == 'Equilátero':
        return 'https://escolaeducacao.com.br/wp-content/uploads/2020/06/triangulo-equilatero.png'
    if formato == 'Isósceles':
        return 'https://static.escolakids.uol.com.br/2020/03/triangulo-isosceles.jpg'
    if formato == 'Escaleno':
        return 'https://static.todamateria.com.br/upload/tr/ia/trianguloescaleno.jpg'