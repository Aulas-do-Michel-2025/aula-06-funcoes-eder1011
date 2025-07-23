"""
Exercício 3 - Calculando a média de uma lista

Escreva uma funcao chamada `calcular_media` (sem acento) que recebe uma lista com numeros
e retorne a média dos valores dela.

Exemplo de uso:
>>> print(calcular_media([0, 100, 200]))
>>> 100
"""
def calcular_media(numeros):
    if not numeros:
        return 0  
    return sum(numeros) / len(numeros)


print(calcular_media([0, 100, 200]))  
