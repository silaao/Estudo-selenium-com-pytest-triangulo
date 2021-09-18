#Para executar esse script, digitar o comando " python script.py " no terminal
from triangulo import defineFormato

lado1 = float(input('Primeiro lado: '))
lado2 = float(input('Segundo  lado: '))
lado3 = float(input('Terceiro lado: '))

retorno = defineFormato(lado1, lado2, lado3)

print(retorno)