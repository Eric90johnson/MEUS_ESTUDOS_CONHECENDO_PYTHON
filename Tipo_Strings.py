"""
Tipo String

Em Python, um dado (variável), é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string´, '234', 'a', 'true', '42.2'
- Estiver entre aspas duplas -> "uma string", "234", "a", "true", "42.2"
- Estiver entre as aspas simples tripla -> '''uma string''', ''''234''', '''a''', '''true''', '''42.2'''
nome = 'Eric Johnson'
print(nome)
print(type(nome))

nome = "Eric´s Johnson"
print(nome)
print(type(nome))

nome = 'Eric \nJohnson'
print(nome)
print(type(nome))

nome = tres aspas Eric
Johnson três aspas
print(nome)
print(type(nome))

nome = "Eric \" Johnson"
print(nome)
print(type(nome))

nome = 'Eric Johnson'
print(nome.upper())

nome = 'Eric Johnson'
print(nome.lower())

nome = 'Eric Johnson'
print(nome.split()) transforma em uma lista de strings


# [ 0,   1,   2,   3,   4,  5,   6,   7,   8,   9,   10,  11]
# ['E', 'r', 'i', 'c', '', 'J', 'o', 'h', 'n', 's', 'o', 'n']

nome = 'Eric johnson'
print(nome[0:4])  # Slice de string

print(nome[5:12])  # Slice de string

# [   0,       1    ]
# ['Eric', 'Johnson']
print(nome.split()[0])

print(nome.split()[1])
"""
# Estiver entre aspas simples triplas -> """uma string""", """234""", """a""", """true""", """42.2"""

nome = 'Eric johnson'

print(nome[::-1])  # inversão da string

# [::-1] -> Comece do primeiro elemento, vá até o ultimo e inverta











