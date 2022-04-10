""""
Tipo Float

Tipo real, decimal

Casas decimais
OBS. O separador de casas decimais em programação é ponto e não a virgula.

"""

# errado do ponto de vista do float, mas gera uma tupla
valor = 1, 44
print(valor)

# certo do ponto de vista float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
Ao converter valores float para inteiro, nós perdemos precisão.
"""
res = int(valor1)
print(res)
print(type(res))

# podemos trabalhar com números complexos "numero acrescentado de J
variavel = 5j





