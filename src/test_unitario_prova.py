from triangulo import defineFormato

def test_triangulo_equilatero():
  formatoEsperado = 'Equilátero'
  formato = defineFormato(10, 10, 10)
  assert formatoEsperado == formato

def test_triangulo_escaleno():
  formatoEsperado = 'Escaleno'
  formato = defineFormato(9, 8, 12)
  assert formatoEsperado == formato

def test_triangulo_isosceles():
  formatoEsperado = 'Isósceles'
  formato = defineFormato(10, 10, 12)
  assert formatoEsperado == formato

def test_todos_lados_igual_zero():
  formatoEsperado = 'Não é um triângulo'
  formato = defineFormato(0, 0, 0)
  assert formatoEsperado == formato