import ast
import math




def calcular_taxa_erro_software(erros, linhas_codigo):
    try:
        erros = float(erros)
        linhas_codigo = float(linhas_codigo)
        return (erros / linhas_codigo) * 100
    except ValueError:
        return None



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
