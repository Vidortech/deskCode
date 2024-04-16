import ast
import math


# Fórmula para cálculo de Bháskara
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


# Fórmula para cálculo de log Simples
def logaritmo(num):
    math.log(num)




# Fórmula para cálculo de complexidade ciclomática


import ast

def calcular_complexidade_ciclomatica(source_code):
    tree = ast.parse(source_code)
    complexity = 1  # Começa com 1 para contar o nó raiz

    for node in ast.walk(tree):
        if isinstance(node, ast.If) or isinstance(node, ast.For) or isinstance(node, ast.While):
            complexity += 1
        elif isinstance(node, ast.FunctionDef):
            # Conta o número de pontos de decisão nas funções
            for sub_node in ast.walk(node):
                if isinstance(sub_node, ast.If) or isinstance(sub_node, ast.For) or isinstance(sub_node, ast.While):
                    complexity += 1
    return complexity

    



        # 

            #
             
                # TERMINAR DE ARRUMAR A FUNÇÃO DE CÁLCULO DE COMPLEXIDADE CICLOMÁTICA

            # 

        # 








# Fórmula para cálculo de velocidade média.
def calcular_velocidade_media(distancia, tempo):
    try:
        distancia = float(distancia)
        tempo = float(tempo)
        velocidade_media = distancia / tempo
        return velocidade_media
    except ValueError:
        return None

# Fórmula para cálculo de força
def calcular_forca_massa_aceleracao(massa, aceleracao):
    try:
        massa = float(massa)
        aceleracao = float(aceleracao)
        forca = massa * aceleracao
        return forca
    except ValueError:
        return None
