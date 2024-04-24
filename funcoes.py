import math


def calcular_velocidade_media(distancia, tempo):
    try:
        distancia = float(distancia)
        tempo = float(tempo)
        return distancia / tempo
    except ValueError:
        return None

def calcular_forca_massa_aceleracao(massa, aceleracao):
    try:
        massa = float(massa)
        aceleracao = float(aceleracao)
        return massa * aceleracao
    except ValueError:
        return None

def bhaskara(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return "Não há raízes reais."
        elif delta == 0:
            x = -b / (2 * a)
            return f'A única raiz é {x:.2f}.'
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return f'As raízes são {x1:.2f} e {x2:.2f}.'
    except ValueError:
        return "Por favor, insira valores numéricos."

def calcular_taxa_erro_software(num_erros, linhas_codigo):
    try:
        num_erros = float(num_erros)
        linhas_codigo = float(linhas_codigo)
        return (num_erros / linhas_codigo) * 100
    except ValueError:
        return None

def calcular_equacao_movimento(velocidade_inicial, aceleracao, tempo):
    try:
        velocidade_inicial = float(velocidade_inicial)
        aceleracao = float(aceleracao)
        tempo = float(tempo)
        return velocidade_inicial * tempo + 0.5 * aceleracao * tempo ** 2
    except ValueError:
        return None
