"""
 Loop for

 Loop -> Estrutura de repetição.
 For - > Uma dessas estruturas.

# Variáveis da aula:
nome = 'Eric Johnson'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # temos que transformar em lista.


C ou Java

for(int i = 0; i < 10; i++) {
    //execução de loop
}

Python

for item in interval:
    // execução de loop

Utilizamos loops para alterar sobre sequencias ou sobre valores inteiráveis.

Exemplos de inteiráveis:
- Strings
    nome = 'eric johnson'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    números = range(1, 10)

# Exemplo de for 1 (Inteirando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (inteirando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Inteirando sobre um range)

range(valor_inicial, valor_final)
Obs.: O valor final não é inclusivo.
1
2
3
4
5
6
7
8
9
10 - não

for numero in range(1, 10):
    print(numero)

Enumerate:

((0, 'E'), (1, 'r'), (2 'i'), (3, 'c'), (4, ' ')...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
Obs.: Quando não precisamos de um valor podemos descarta-lo usando (_)

for valor in enumerate(nome):
    print(valor)

for valor in enumerate(nome):
    print(valor[0])

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

"""

