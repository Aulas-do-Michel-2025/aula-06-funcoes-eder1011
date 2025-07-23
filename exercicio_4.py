"""
Exercicio 4 - Usando funcoes

Você vai escrever uma funcao que recebe uma lista com números e deve retornar uma outra lista
só com os números primos.

Mas você não precisa escrever a lógica para saber se o número é primo: você pode só usar a funcão
`verificar_se_eh_primo` disponibilizada, que vai retornar True se o número for primo e False se não for.

"""

def filtrar_primos(lista):
   
    if not isinstance(lista, list):
        raise TypeError("A entrada deve ser uma lista.")

    primos = []
    for numero in lista:
        if verificar_se_eh_primo(numero):
            primos.append(numero)
    return primos
