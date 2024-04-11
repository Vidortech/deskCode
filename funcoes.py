def bhaskara(n1, n2, n3):
  n1 = float(input('Digite o valor de a: '))
  n2 = float(input('Digite o valor de b: '))
  n3 = float(input('Digite o valor de c: '))
  delta = (n2**2) - 4 * n1 * n3
  
  if delta < 0:
    print('Não existe raiz real')
  elif delta == 0:
    print('Existe apenas uma raiz real')
    root = (-n2 + math.sqrt(delta) / (2 * n1))
    print(f'A raiz é: {root}')
  else:
    print('Existem duas raizes reais')
    root1 = (-n2 + math.sqrt(delta)) / (2 * n1)
    root2 = (-n2 - math.sqrt(delta)) / (2 * n1)
    print(f'As raizes são: {root1} e {root2}')

  bhaskara(0.0, 0.0, 0.0)