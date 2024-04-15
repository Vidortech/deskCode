
import math

def bhaskara(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        delta = b**2 - 4 * a * c

        if delta < 0:
            return 'Não existem raízes reais.'
        elif delta == 0:
            root = -b / (2 * a)
            return f'Existe apenas uma raiz real: {root:.2f}'
        else:
            root1 = (-b + math.sqrt(delta)) / (2 * a)
            root2 = (-b - math.sqrt(delta)) / (2 * a)
            return f'As raízes são: {root1:.2f} e {root2:.2f}'  
    except ValueError:
        return 'Os coeficientes devem ser números.'


def logaritmo(num):
    math.log(num)




